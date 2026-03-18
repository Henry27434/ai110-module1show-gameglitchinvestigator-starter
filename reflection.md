# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The same looked fine as I ran it and every clickable box was working and displayed what they needed, such as the Developer Debug info.
The first bug was that wrong guesses were sometimes increasing my score total after a few playthroughs, and another bug I found was that the hints were backwards with some numbers where it needed to say "Go Higher!" instead of lower.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Copilot throughout the Project. When I described the reversed hints bug and shared the check_guess function, Copilot correctly identified that the return values for "Too High" and "Too Low" had swapped messages. When I asked Copilot about the even/odd string casting section, Copilot's first response described it as "an intentional difficulty mechanic to add unpredictability." Which I analyzed as CoPilot thinking it were intentional.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I would reproduce the mistake by purposing trying to get the wrong hint to appear, make the fix so it wouldn't be reversed, and retested it along with adding pytest cases. For the hint reversal, I added test_hint_too_high_says_go_lower, and after the fix it gave would work rather than fail with the old version. Adding to the evidence for the last question. Copilot helped me understand why the test for test_wrong_guess_always_decreases_score should target even attempt numbers specifically, which pointed me at the attempt_number % 2 == 0 condition as the primary cause.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit was rerunning the entire code every time the Users interacts with the page. Session state was able to fix this by keeping a different state, or versions of the page, like cookies. So checking if a secret was in the current state and generating a new one based on this would allow for Streamlit to not cause issues.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I will keep is the "breaks" with comments on each line that was identified to contain an "error" which made it simplier to break down the entire program into smaller sections. FOr my next time I work with AI, I will try and utilize it less and less and see how far I can go without it or letting it analyze makor sections before me. This project let me see that just because the code can run, does not mean that it will be correct at all for the requirements or goals intended. 