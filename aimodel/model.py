from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)


#Keep XML tags to delimit each section of the input. E.g. <resume> and <jobApplication>. Can also delimit sections of the resume as well.
#Ask for structured output, such as JSON with list of strengths, list of weaknesses, star_rating.
#Provide an example of a structured answer
# Provide step by step instructions, e.g. 1. DO A 2. Do B, 3. Do c