def guess_number():
    low = 1
    high = 100
    guess = 0
    
    print("0から100までの数字を考えてください。")
    
    while True:
        guess = (low + high) // 2
        print("私の考えで数字は", guess, "ですか？")
        user_input = input("あたったのであれば「あたりました。」、小さければ「小さいです。」、大きければ「大きいです。」と入力してください。: ")
        
        if user_input == "あたりました。":
            print("正解です！")
            break
        elif user_input == "小さいです。":
            high = guess - 1
        elif user_input == "大きいです。":
            low = guess + 1
        else:
            print("間違った入力です。「あたりました。」、「小さいです。」、「大きいです。」の中で選んでください。")

guess_number()