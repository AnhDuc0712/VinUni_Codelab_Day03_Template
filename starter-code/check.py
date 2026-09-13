from template import ChatbotBaseline, ReActAgent

query = "Tìm chuyến bay từ HAN đi SGN dưới 2 triệu, và thời tiết SGN nên mặc gì?"

print("=== BASELINE ===")
print(ChatbotBaseline().query(query))

print("\n=== REACT ===")
agent = ReActAgent(max_iterations=5)
result = agent.run(query)

print("STATUS:", result.get("status"))
print("ANSWER:", result.get("answer"))
print("ITERATIONS:", result.get("iterations"))
print("TRACE:")
for step in result.get("trace", []):
    print(step)