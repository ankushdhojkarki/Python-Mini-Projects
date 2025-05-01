questions = [
    ["1. What is the capital city of Australia?", "A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane", 3],
    ["2. Who wrote the play 'Romeo and Juliet'?", "A. William Wordsworth", "B. William Shakespeare", "C. Charles Dickens", "D. George Orwell", 2],
    ["3. What is the largest planet in our solar system?", "A. Earth", "B. Mars", "C. Saturn", "D. Jupiter", 4],
    ["4. In which country were the Olympic Games originated?", "A. Nepal", "B. Australia", "C. Greece", "D. Azerbaijan", 3],
    ["5. What is the chemical symbol for gold?", "A. Au", "B. Ag", "C. Gd", "D. Go", 1],
    ["6. How many continents are there on Earth?", "A. 5", "B. 6", "C. 7", "D. 8", 3],
    ["7. Which artist painted the Mona Lisa?", "A. Pablo Picasso", "B. Vincent van Gogh", "C. Claude Monet", "D. Leonardo da Vinci", 4],
    ["8. What is the tallest mountain in the world?", "A. Mount Everest", "B. K2", "C. Lhotse", "D. Kanchenjunga", 1],
    ["9. Which planet is known as the 'Red Planet'?", "A. Mars", "B. Mercury", "C. Neptune", "D. Jupiter", 1],
    ["10. What is the smallest prime number?", "A. 0", "B. 1", "C. 2", "D. 3", 3]
]

prizes = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]

i = 0
for question in questions:
    print(question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4])
    
    answer = input("Enter your answer (a, b, c, d): ").lower()
    
    if answer == 'a':
        user_choice = 1
    elif answer == 'b':
        user_choice = 2
    elif answer == 'c':
        user_choice = 3
    elif answer == 'd':
        user_choice = 4
    else:
        print("Invalid input! Please enter a, b, c, or d.")
        break

    if user_choice == question[5]:
        print("Correct Answer.")
        print(f"You won ₹{prizes[i]}")
        i += 1
    else:
        correct_option = ['A', 'B', 'C', 'D'][question[5] - 1]
        print(f"Wrong, the correct answer is {correct_option}.")
        print("Better luck next time!")
        break
