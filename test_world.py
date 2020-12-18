# -*- coding: utf-8 -*-

import pytest

import program.world as script


####################################
########        AGENT       ########
####################################

class TestAgent:

    def setup_method(self):
        self.agent = script.Agent(3)

    #   - recuperer un attribut position
    def test_get_position(self):
        assert self.agent.position == 3

    #   - modifier un attribut position
    def test_set_position(self):
        self.agent.position = 5
        assert self.agent.position == 5

    #   - assigner un dictionnaire en tant qu'attributs
    def test_set_agent_attributes(self):
        agent = script.Agent(3, agreeableness=-1)
        assert agent.agreeableness == -1


#######################################
########        POSITION       ########
#######################################

class TestPosition:

    def setup_method(self):
        self.POSITION = script.Position(100, 33)

    #   - modifier un attribut longitude degrees
    def test_longitude_degrees(self):
        assert self.POSITION.longitude_degrees == 100

    #   - modifier un attribut latitude degrees
    def test_latitude_degrees(self):
        assert self.POSITION.latitude_degrees == 33

    #   - recuperer une longitude
    def test_longitude(self):
        print('longitude', self.POSITION.longitude)
        assert self.POSITION.longitude == 1.7453292519943295

    #   - recuperer une latitude
    def test_latitude(self):
        print('latitude', self.POSITION.latitude)
        assert self.POSITION.latitude == 0.5759586531581288

    #   - verifier la valeur d'une latitude
    def test_latitude_degrees_range(self):
        with pytest.raises(AssertionError):
            position = script.Position(100, 100)


####################################
########        ZONES       ########
####################################

class TestZone:

    def setup_method(self):
        self.position1 = script.Position(100, 33)
        self.position2 = script.Position(101, 34)
        self.zone = script.Zone(self.position1, self.position2)
        script.Zone._initialize_zones()
        agent = script.Agent(self.position1, agreeableness=1)
        self.zone.inhabitants = [agent]

    def teardown_method(self):
        script.Zone.ZONES = []

    #   - recuperer toutes les instances Zone
    def test_get_zones(self):
        assert len(self.zone.ZONES) == 64800



############################################
########        AGREEABLENESS       ########
############################################

class TestAgreeableness:

    @classmethod
    def setup_class(cls):
        script.Zone._initialize_zones()
        cls.ZONE = script.Zone.ZONES[0]
        cls.GRAPH = script.AgreeablenessGraph()
        cls.ZONES = script.Zone.ZONES
        for _ in range(0,10):
            cls.ZONE.add_inhabitant(script.Agent(script.Position(-180, -89), agreeableness=1))

    #- Récupérer un titre
    def test_title(self):
        assert self.GRAPH.title == "Nice people live in the countryside"

    #- Récupérer x_label
    def test_x_label(self):
        assert self.GRAPH.x_label == "population density"

    #- Récupérer y_label
    def test_y_label(self):
        assert self.GRAPH.y_label == "agreeableness"

    #- Récupérer xy_values sous forme de tuples
    def test_xy_values(self):
        assert len(self.GRAPH.xy_values(self.ZONES)) == 2

    #- La première valeur de xy_values est la densité de population moyenne pour la première zone
    def test_average_population_density(self):
        assert self.GRAPH.xy_values(self.ZONES)[0][0] == self.ZONE.population_density()

    #- La seconde valeur de xy_values est l'agréabilité moyenne
    def test_average_agreeableness(self):
        assert self.GRAPH.xy_values(self.ZONES)[1][0] == self.ZONE.average_agreeableness()
