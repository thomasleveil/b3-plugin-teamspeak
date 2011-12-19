from tests import *
prepare_fakeparser_for_tests()

import unittest
import b3
from b3.config import XmlConfigParser
from teamspeak import TeamspeakPlugin



class Test_config_teamspeakChannels(unittest.TestCase):

    def test_default_values(self):
        conf = XmlConfigParser()
        conf.setXml("""
        <configuration plugin="teamspeakbf">
        	<settings name="teamspeakServer">
                <set name="host">foo_host</set>
                <set name="queryport">foo_queryport</set>
                <set name="id">1</set>
                <set name="login">foo_login</set>
                <set name="password">foo_password</set>
            </settings>
        </configuration>
        """)
        p = TeamspeakPlugin(fakeConsole, conf)
        p.readConfig()
        self.assertEqual(TeamspeakPlugin.TS3ChannelB3, p.TS3ChannelB3)
        self.assertEqual(TeamspeakPlugin.TS3ChannelTeam1, p.TS3ChannelTeam1)
        self.assertEqual(TeamspeakPlugin.TS3ChannelTeam2, p.TS3ChannelTeam2)

    def test_nominal(self):
        conf = XmlConfigParser()
        conf.setXml("""
        <configuration plugin="teamspeakbf">
        	<settings name="teamspeakServer">
                <set name="host">foo_host</set>
                <set name="queryport">foo_queryport</set>
                <set name="id">1</set>
                <set name="login">foo_login</set>
                <set name="password">foo_password</set>
            </settings>
            <settings name="teamspeakChannels">
                <set name="B3">channel name</set>
                <set name="team1">Team 1 name</set>
                <set name="team2">Team 2 name</set>
                <set name="DefaultTarget">team</set>
            </settings>
        </configuration>
        """)
        p = TeamspeakPlugin(fakeConsole, conf)
        p.readConfig()
        self.assertEqual('channel name', p.TS3ChannelB3)
        self.assertEqual('Team 1 name', p.TS3ChannelTeam1)
        self.assertEqual('Team 2 name', p.TS3ChannelTeam2)



if __name__ == '__main__':
    unittest.main()
