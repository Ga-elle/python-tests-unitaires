# -*- coding: utf-8 -*-

import pytest

import program.world as script


#- Agent : 

agent = script.Agent('3')
    
#   - recuperer un attribut position
def test_get_position():
    agent = script.Agent(3)
    assert agent.position == 3
    
#   - modifier un attribut position
def test_set_position():
    agent = script.Agent(3)
    agent.position = 5
    assert agent.position == 5
    
#   - assigner un dictionnaire en tant qu'attributs
def test_set_agent_attributes():
    agent = script.Agent(3, agreeableness=1)
    assert agent.agreeableness == 1
    
#- Position

#   - modifier un attribut longitude degrees
def test_longitude_degrees():
    position = script.Position(100, 34)
    assert position.longitude_degrees == 100
    
#   - modifier un attribut latitude degrees
def test_latitude_degrees():
    position = script.Position(100, 34)
    assert position.latitude_degrees == 34
    
#   - recuperer une longitude
def test_longitude():
    position = script.Position(100, 33)
    print('longitude', position.longitude)
    assert position.longitude == 1.7453292519943295
     
#   - recuperer une latitude
def test_latitude():
    position = script.Position(100, 33)
    print('latitude', position.latitude)
    assert position.latitude == 0.5759586531581288
    
#   - verifier la valeur d'une latitude
def test_latitude_degrees_range():
    with pytest.raises(AssertionError):
        position = script.Position(100, 100)