from py_rete.utils import parse_xml
from py_rete.common import Rule
from py_rete.common import Has
from py_rete.common import Ncc
from py_rete.common import Filter
from py_rete.common import Bind


def test_xml():
    s = """<?xml version="1.0"?>
    <data version="0.0.2">
        <production>
            <lhs>
                <has identifier="$x" attribute="on" value="$y" />
                <bind to="$test">1+1</bind>
                <filter>$y != "table"</filter>
                <ncc>
                    <has identifier="$z" attribute="color" value="red" />
                    <has identifier="$z" attribute="on" value="$w" />
                </ncc>
            </lhs>
            <rhs></rhs>
        </production>
    </data>"""
    result = parse_xml(s)
    assert result[0][0] == Rule(
        Has('$x', 'on', '$y'),
        Bind('1+1', '$test'),
        Filter('$y != "table"'),
        Ncc(Has('$z', 'color', 'red'),
            Has('$z', 'on', '$w')))
