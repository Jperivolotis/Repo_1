startTime = datetime(2023, 7, 27, 12, 0, 0);
stopTime = startTime + days(4);
sampleTime = 90;
sc = satelliteScenario(startTime, stopTime, sampleTime);

semiMajorAxis = 6821000;
eccentricity = 0;
inclination = 90;
rightAscensionOfAscendingNode = 0;
argumentOfPeriapsis = 0;
trueAnomaly = 0;

sat = satellite(sc,semiMajorAxis, eccentricity,inclination,rightAscensionOfAscendingNode,...   
         argumentOfPeriapsis, trueAnomaly, "OrbitPropagator", "two-body-keplerian", "Name", "Sat");
g = gimbal(sat);
camsensor = conicalSensor(g, MaxViewAngle=130);

v = satelliteScenarioViewer(sc, "Dimension", "2D");
fieldOfView(camsensor);
leadTime = 3600;                                         % seconds
trailTime = 2*3600;
gt = groundTrack(sat,"LeadTime",leadTime,"TrailTime",trailTime);
play(sc)

