import random

print('==================================================================')
mode = input('請選擇遊玩模式\n1.正常四字模式 2.困難五字模式 3.挑戰限制次數 4.籌碼模式：')
print('==================================================================')


if mode == '1':

    print('開始【正常四字模式】！')

    answer = '' 
    a_count=0 
    b_count=0 

    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    random.shuffle(items)
    for i in range(4):
        answer+=str(items[i])

    while(True):

        number = input('Enter the number: ')

        if not number.isdigit() or len(number) != 4: 
            print('Please enter four digits！')

        # 判斷輸入的值是否有重複
        elif len(set(number)) < 4:
            print('您輸入的數字中有重複值，請重新輸入！')

        else:

            if number == answer:
                print('excellent you guess the correct number！')
                break

            for i in range(4):
                for j in range(4):
                    if i==j and number[i]==answer[j]:
                        a_count+=1
                    elif number[i]==answer[j]:
                        b_count+=1
            print('{0}A{1}B'.format(a_count,b_count))

            a_count=0
            b_count=0

elif mode == '2':

    print('開始【困難五字模式】！')

    answer = '' 
    a_count=0 
    b_count=0 

    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    random.shuffle(items)
    for i in range(5):
        answer+=str(items[i])

    while(True):

        number = input('Enter the number: ')

        if not number.isdigit() or len(number) != 5: 
            print('Please enter five digits！')

        # 判斷輸入的值是否有重複
        elif len(set(number)) < 5:
            print('您輸入的數字中有重複值，請重新輸入！')

        else:

            if number == answer:
                print('excellent you guess the correct number！')
                break

            for i in range(5):
                for j in range(5):
                    if i==j and number[i]==answer[j]:
                        a_count+=1
                    elif number[i]==answer[j]:
                        b_count+=1
            print('{0}A{1}B'.format(a_count,b_count))

            a_count=0
            b_count=0

elif mode == '3':

    print('開始【挑戰限制次數】！')

    answer = '' 
    a_count=0 
    b_count=0 

    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    random.shuffle(items)
    for i in range(4):
        answer+=str(items[i])

    limit = int(input('請輸入欲挑戰的限制次數：'))

    while(limit > 0):

        number = input('Enter the number: ')

        if not number.isdigit() or len(number) != 4: 
            print('Please enter four digits！')

        # 判斷輸入的值是否有重複
        elif len(set(number)) < 4:
            print('您輸入的數字中有重複值，請重新輸入！')

        else:

            if number == answer:
                print('excellent you guess the correct number！')
                break

            for i in range(4):
                for j in range(4):
                    if i==j and number[i]==answer[j]:
                        a_count+=1
                    elif number[i]==answer[j]:
                        b_count+=1
            print('{0}A{1}B'.format(a_count,b_count))

            limit-=1
            a_count=0
            b_count=0

    print('==================================================================')
    if limit == 0 and number != answer:
        print('挑戰失敗！')
        print('答案為：{0}'.format(answer))

elif mode == '4':

    print('開始【籌碼模式】！')
    print('在籌碼模式中，玩家可以先輸入想擁有的籌碼數目，如果在五次以內猜出答案不會扣除籌碼，如果超過五次才猜出答案，則會扣除一枚籌碼！')
    print('快來試試看擁有籌碼的你，能完成幾次遊戲吧！')

    answer = '' 
    a_count=0 
    b_count=0 

    coins = int(input('請輸入想擁有的籌碼數目（1~5枚）：'))
    game_complete = 0

    while(coins > 0):

        answer = ''
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        random.shuffle(items)
        for i in range(4):
            answer+=str(items[i])
        game_count = 0

        while(True):
            number = input('Enter the number: ')
            if not number.isdigit() or len(number) != 4: 
                print('Please enter four digits！')
            elif len(set(number)) < 4:
                print('您輸入的數字中有重複值，請重新輸入！')
            else:
                if number == answer:
                    if game_count > 5:
                        coins-=1
                    print('excellent you guess the correct number！')
                    print('剩餘籌碼{0}枚'.format(coins))
                    game_complete+=1
                    break

                for i in range(4):
                    for j in range(4):
                        if i==j and number[i]==answer[j]:
                            a_count+=1
                        elif number[i]==answer[j]:
                            b_count+=1
                print('{0}A{1}B'.format(a_count,b_count))
                
                game_count+=1
                a_count=0
                b_count=0

    print('==================================================================')
    print('結果公布！')
    print('你完成了{0}場遊戲！'.format(game_complete))



    