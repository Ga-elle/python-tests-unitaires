# -*- coding: utf-8 -*-

import pytest
import program.download_agents as script

import urllib.request
from io import BytesIO
import json


def test_http_return1(monkeypatch):
    """Utiliser un mock"""

    results = [{
        "age": 84,
        "agreeableness": 0.74
    }]

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    assert script.get_agents(1) == results


def test_http_return2(tmpdir, monkeypatch):
    """Utiliser un mock et imiter l'écriture dans un fichier"""

    results = [{
        "age": 84,
        "agreeableness": 0.74
    }]
    
    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    p = tmpdir.mkdir("program").join("agents.json")

    #- Run script
    script.main(["--dest", str(p), "--count", "1"])

    local_res = json.load(open(p))
    assert script.get_agents(1) == local_res
