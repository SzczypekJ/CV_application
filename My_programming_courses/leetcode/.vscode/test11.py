def solution(stationsA, stationsB, stationsC, origin, destination):
    if destination not in stationsA and destination not in stationsB and destination not in stationsC:
        return ""
    else:
        if (origin in stationsA and destination in stationsB) or (origin in stationsB and destination in stationsA):
            return "AB"
        elif (origin in stationsB and destination in stationsC) or (origin in stationsC and destination in stationsB):
            return "BC"
        else:
            return "ABC"

# print(solution(stationsA=["Green Park", "Holborn"], stationsB=["Mile End", "Bow Road"], stationsC=[
#     "Forest Hill", "Balham"], origin="Mile End", destination="Bow Road"))
# def solution(stationsA, stationsB, stationsC, origin, destination):
#     if destination not in stationsA and destination not in stationsB and destination not in stationsC:
#         return ""
#     else:
#         if (origin in stationsA and destination in stationsB) or (origin in stationsB and destination in stationsA):
#             return "AB"
#         elif (origin in stationsB and destination in stationsC) or (origin in stationsC and destination in stationsB):
#             return "BC"
#         elif (origin in stationsA and destination in stationsC) or (origin in stationsC and destination in stationsA):
#             return "AC"
#         else:
#             return "ABC"


stationsA = ["Willesden Junction", "Southfields", "Queensway",
             "Park Royal", "Canons Park", "Finchley Central"]
stationsB = ["Heathrow Terminal 5", "Latimer Road",
             "Ruislip Gardens", "Canada Water"]
stationsC = ["Northolt", "Barons Court", "Hanger Lane", "Hounslow Central",
             "Hampstead", "Wood Green", "King's Cross", "Hounslow West", "Kennington", "Watford"]
origin = "Hounslow Central"
destination = "Wood Green"

print(solution(stationsA, stationsB, stationsC, origin, destination))
