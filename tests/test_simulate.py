import blah


def test_simulate():
    s = blah.Simulation()
    u = s.calculate()
    assert (u > 0).any()

def test_initial_conditions():
    s = blah.Simulation()
    print(s.u[0,s.plate_length-1,:])
    assert s.u[0,s.plate_length-1,5] == 100.
