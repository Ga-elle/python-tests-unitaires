# -*- coding: utf-8 -*-

import pytest

import program.world as script


####################################
########        AGENT       ########
#################################### 

class TestAgent:
    AGENT = script.Agent(3)
        
    #   - recuperer un attribut position
    def test_get_position(self):
        assert self.AGENT.position == 3
        
    #   - modifier un attribut position
    def test_set_position(self):
        self.AGENT.position = 5
        assert self.AGENT.position == 5
        
    #   - assigner un dictionnaire en tant qu'attributs
    def test_set_agent_attributes(self):
        agent = script.Agent(3, agreeableness=1)
        assert agent.agreeableness == 1
    

#######################################
########        POSITION       ########
#######################################

class TestPosition:
    
    POSITION = script.Position(100, 33)
    
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
    POSITION1 = script.Position(100, 33)
    POSITION2 = script.Position(101, 34)
    ZONE = script.Zone.find_zone_that_contains(POSITION1)
    AGENT = script.Agent(POSITION1, agreeableness=1)
    
    #   - recuperer toutes les instances Zone
    def test_get_zones(self):
        assert len(self.ZONE.ZONES) == 64800
        
