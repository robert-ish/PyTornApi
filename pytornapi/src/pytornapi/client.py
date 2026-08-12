import requests
import time

from .exceptions import TornAPIError
from .exceptions import RateLimitError
from .exceptions import InvalidKeyError
from .exceptions import TornAPIResponseError

from .enums import UserField
from .enums import PropertyField
from .enums import FactionField
from .enums import CompanyField
from .enums import MarketField
from .enums import TornField

class TornAPI:
    """Creates a TornAPI object (or whatever). First argument is your API key.\n
    For more info, see docstring on the library itself.
    """
    BASE_URL = "https://api.torn.com/"

    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
        self.last_request_time = 0

    def _call(self, endpoint, params=None):
        """Gets and returns something from Torn's API. supposed to only be used by the class itself"""

        url = f"{self.BASE_URL}{endpoint}"
        params = params or {}
        params["key"] = self.api_key

        response = self.session.get(url, params=params)
        self.last_request_time = time.time()

        data = response.json()
        if "error" in data:
            err = data["error"]
            if isinstance(err, dict):
                code = err.get("code")
                msg = err.get("error", "Unknown error")
                if code == 2:
                    raise InvalidKeyError(msg)
            else:
                raise TornAPIError(str(err))
        if data.get("rate_limited"):
            retry_after = data.get("retry_after", 'Unknown')
            raise RateLimitError(
                f"Rate limit exceeded. Try again in {retry_after} seconds.",
                retry_after=retry_after
            )
        if response.status_code != 200:
            raise TornAPIResponseError(f"Torn API didnt respond: status code {response.status_code}")

        return data

    def get_user(self, user_id: int, selections: UserField | str | None = None):
        """Gets a user from a user id.
        Available selections:
        ammo, attacks, attacksfull, bars, basic, battlestats, 
        bazaar, bounties, calendar, casino, competition, 
        cooldowns, crimes, criminalrecord, discord, display, 
        education, enlistedcars, equipment, events, faction, 
        forumfeed, forumfriends, forumposts, forumsubscribedthreads, 
        forumthreads, gym, hof, honors, icons, inventory, itemmarket, 
        itemmods, job, jobpoints, jobranks, list, log, lookup, 
        medals, merits, messages, missions, money, networth, 
        newevents, newmessages, notifications, organizedcrime, 
        organizedcrimes, perks, personalstats, profile, properties, 
        property, races, racingrecords, refills, reports, revives, 
        revivesfull, skills, snapshot, stocks, timestamp, trade, 
        trades, travel, virus, weaponexp, workstats"""
        params = {"selections": selections} if selections else {}
        return self._call(f"user/{user_id}", params)
    def get_property(self, property_id, selections: PropertyField | str | None = None):
        """Gets a property from a property ID.
        Available selections:
        lookup, property, timestamp"""
        params = {"selections": selections} if selections else {}
        return self._call(f"property/{property_id}", params)
    def get_faction(self, faction_id, selections: FactionField | str | None = None):
        """Gets a faction from a faction ID.
        Available selections:
        applications, armor, armorynews, 
        attacknews, attacks, attacksfull, 
        balance, basic, boosters, caches, 
        cesium, chain, chainreport, chains, 
        contributors, crime, crimeexp, 
        crimenews, crimes, currency, 
        donations, drugs, fundsnews, hof, 
        lookup, mainnews, medical, members, 
        membershipnews, news, positions, 
        rackets, raidreport, raids, rankedwarreport, 
        rankedwars, reports, revives, 
        revivesfull, search, snapshot, 
        stats, temporary, territory, 
        territorynews, territoryownership, 
        territorywarreport, territorywars, 
        timestamp, upgrades, utilities, 
        warfare, wars, weapons
        """
        params = {"selections": selections} if selections else {}
        return self._call(f"faction/{faction_id}", params)
    def get_company(self, company_id, selections: CompanyField | str | None = None):
        """Gets a company from a company ID.
        Available selections:
        applications, companies, detailed, 
        employees, lookup, news, profile, 
        search, snapshot, stock, timestamp"""
        params = {"selections": selections} if selections else {}
        return self._call(f"company/{company_id}", params)
    def get_market(self, market_id, selections: MarketField | str | None = None):
        """Gets a market from a market ID.
        Available selections:
        auctionhouse, auctionhouselisting, bazaar, itemmarket, lookup, pointsmarket, properties, rentals, timestamp"""
        params = {"selections": selections} if selections else {}
        return self._call(f"market/{market_id}", params)
    
    def get_torn(self, torn_id, selections: TornField | str | None = None):
        """Gets basically anything, from a torn ID.
        I have no idea what torn ID does im sorry.
        Available selections:
        attacklog, bank, bounties, calendar, cards, chainreport, cityshops, companies, competition, crimes, dirtybombs, education, elimination, eliminationteam, factionhof, factiontree, gyms, hof, honors, itemammo, itemdetails, itemmods, items, itemstats, logcategories, logtypes, lookup, medals, merits, museum, organisedcrimes, organizedcrimes, pawnshop, pokertables, properties, rackets, raidreport, raids, rankedwarreport, rankedwars, rockpaperscissors, searchforcash, shoplifting, stats, stocks, subcrimes, territory, territorynames, territorywarreport, territorywars, timestamp"""
        params = {"selections": selections} if selections else {}
        return self._call(f"torn/{torn_id}", params)