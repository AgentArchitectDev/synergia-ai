from ai.memory.memory_manager import memory


print("\n")
print("===================================")
print("SYNERGIA MEMORY SYSTEM TEST")
print("===================================")
print("\n")


memory.save_interaction(
    session_id="maq2_dev",
    model="llama3.2",
    prompt="hola synergia",
    response="Hola Gerardo"
)


memory.save_interaction(
    session_id="maq2_dev",
    model="deepseek-coder-v2",
    prompt="crear navbar moderna",
    response="Navbar creada correctamente"
)


print("\n")
print("===================================")
print("LOAD CONVERSATION")
print("===================================")
print("\n")


conversation = memory.load_conversation("maq2_dev")

for item in conversation:

    print("TIMESTAMP :", item["timestamp"])
    print("MODEL     :", item["model"])
    print("PROMPT    :", item["prompt"])
    print("RESPONSE  :", item["response"])
    print("-----------------------------------")


print("\n")
print("===================================")
print("LIST SESSIONS")
print("===================================")
print("\n")


sessions = memory.list_sessions()

for s in sessions:
    print("SESSION :", s)


print("\n")
print("===================================")
print("LAST MESSAGES")
print("===================================")
print("\n")


last = memory.get_last_messages(
    session_id="maq2_dev",
    limit=2
)

for item in last:

    print(item["prompt"])
    print(item["response"])
    print("-----------------------------------")


print("\n")
print("===================================")
print("SEARCH TEST")
print("===================================")
print("\n")


results = memory.search_in_conversation(
    session_id="maq2_dev",
    keyword="navbar"
)

for item in results:

    print(item["prompt"])
    print(item["response"])
    print("-----------------------------------")


print("\n")
print("===================================")
print("END TEST")
print("===================================")
print("\n")
