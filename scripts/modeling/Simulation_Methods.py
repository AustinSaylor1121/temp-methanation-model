import cantera as ct

def profile_simulation(yaml_file):
    # unit conversion factors to SI
    
    cm = 0.01 # cm to m
    mm = 0.001 # mm to m
    mg = 0.001 # mg to g
    ml = 1e-6 # ml to m^3
    minute = 1 / 60.0 # min to s
    bar = 1e5

    tc = 320 # Temperatuer in Celcius
    t = tc + 273  # Temperature in Kelvin

    p = 1.2 * bar # pressure

    length_total = 100 * mm  # Reactor length
    length_coated = 55 * mm # Coated length

    width = 40 * mm # Reactor width
    height = 5 * mm # reactor height

    area = width * height # cross sectional area

    coated_volume = length_coated * width * height # Volume of the coated section in the reactor

    ni_specific_area = 23.1 # specific surface area of ni in m^2 / g catalyst

    cat_mass = 83.3 * mg # mass of the catalyst 

    cat_area = ni_specific_area * cat_mass # surface area of the catalyst

    cat_area_per_vol = cat_area / coated_volume # Catalyst particle surface area per unit volume

    volumetric_flow_rate = 100 * ml * minute  # volumetric flow rate

    #To start with, I will assume a porisity of 1
    porosity = 1  # Catalyst bed porosity

    # The PFR will be simulated by a chain of 'NReactors' stirred reactors.
    NReactors = 201

    # import the phase models and set the initial conditions
    #create three surface and gas objects to avoid needing to clone the gas/surf

    surf1 = ct.Interface(yaml_file, name='surface1')
    surf1.TP = t, p

    surf2 = ct.Interface(yaml_file, name='surface1')
    surf2.TP = t, p

    surf3 = ct.Interface(yaml_file, name='surface1')
    surf3.TP = t, p

    gas1 = surf1.adjacent['gas']
    gas1.TPX = 25 + 273, ct.one_atm, 'Ar:20, H2(4):64, CO2(2):16'

    gas2 = surf2.adjacent['gas']
    gas2.TPX = t, p, 'Ar:20, H2(4):64, CO2(2):16'

    gas3 = surf3.adjacent['gas']
    gas3.TPX = t, p, 'Ar:20, H2(4):64, CO2(2):16'


    rlen = length_total/(NReactors-1)
    rvol = area * rlen * porosity

    # catalyst area in one reactor
    cat_area = cat_area_per_vol * rvol

    mass_flow_rate = volumetric_flow_rate * gas1.density

    gas1.TPX = t, p, 'Ar:20, H2(4):64, CO2(2):16'

    # create a new reactor
    r = ct.IdealGasReactor(gas1, energy='off', clone=False)
    r.volume = rvol

    # create a reservoir to represent the reactor immediately upstream. Note
    # that the gas object is set already to the state of the upstream reactor
    upstream = ct.Reservoir(gas2, name='upstream',clone=False)

    # create a reservoir for the reactor to exhaust into. The composition of
    # this reservoir is irrelevant.
    downstream = ct.Reservoir(gas3, name='downstream',clone=False)

    # Add the reacting surface to the reactor. The area is set to the desired
    # catalyst area in the reactor.
    rsurf = ct.ReactorSurface(surf1, r, A=cat_area, clone=False)

    # The mass flow rate into the reactor will be fixed by using a
    # MassFlowController object.
    m = ct.MassFlowController(upstream, r, mdot=mass_flow_rate)

    # We need an outlet to the downstream reservoir. This will determine the
    # pressure in the reactor. The value of K will only affect the transient
    # pressure difference.
    v = ct.PressureController(r, downstream, primary=m, K=1e-6)

    sim = ct.ReactorNet([r])

    # print(sim.rtol)
    # print(sim.atol)

    # sim.rtol = 1.0e-11
    # sim.atol = 1.0e-22

    sim.max_time_step = 10

    

    headers = ['Distance (mm)', 'T (C)', 'P (atm)'] + gas1.species_names + surf1.species_names
    output_data = []

    for n in range(NReactors):
        
        dist = n * rlen * 1.0e3  # distance in mm

        # only run in the simulation if over the coated area

        if dist >= 35 and dist <= 90:

            # Set the state of the reservoir to match that of the previous reactor
            upstream.phase.TDY = r.phase.TDY
            sim.reinitialize()
            
            sim.advance_to_steady_state()
            # sim.solve_steady()
        
        # write the gas mass fractions and surface coverages vs. distance
        output_data.append(
            [dist, r.T - 273.15, r.phase.P / ct.one_atm]
            + list(r.phase.X)  
            + list(rsurf.phase.coverages)  
        )

    return headers, output_data