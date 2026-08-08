from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

# res = tavily_search("best hotels in india")
# print(res)



# res = search_flights("Plan a 7 days trip to london ")

# print(res)

res = run_travel_agent("Plan a 7 days trip from india to switzerland")
print(res["answer"])