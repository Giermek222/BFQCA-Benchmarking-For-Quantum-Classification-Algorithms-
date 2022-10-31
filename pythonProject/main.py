# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tgtg import TgtgClient

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = TgtgClient(
        access_token='e30.eyJzdWIiOiI0ODA2ODM0NiIsImV4cCI6MTY2NzQxNjQxOSwidCI6IklsdGw3Q1BGUjY2ekYwbkFCeG9ZQUE6MDoxIn0.ezVwqU4lBsR-Xj8KzAK7F6ImzsSMR0zhHejgg7gJkTA',
        refresh_token='e30.eyJzdWIiOiI0ODA2ODM0NiIsImV4cCI6MTY5ODc3OTYxOSwidCI6Ik1PcG1VVFBUUnUyYWNPcEloZWN0dmc6MDowIn0.aPv7iUFVghgxNIbujezaMZbkUAC4bnkXjRTZKuyt8lY',
        user_id='48068346')
    items = client.get_items()
    for item in items:
        print(item["items_available"])



