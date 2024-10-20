# 1.  Create a program that manages a list of your favorite movies (add, remove, display).
def movie_db():
    favmovies = list(input('enter the movie you wish to add to the listL').split())
    while True:
        action = input('enter the ction you wish to perform as: Add movie to the list, remove movie from the list, display the movie list')
        if action == 'add':
            movies = input('enter the mivie you wish to add to the list saperated by a space:').split()
            for movie in movies:
                favmovies.append(movie.strip())
            print('the mofies added to the list are: ', {','.join(movies)})

        elif action == 'remove':
            moviesr = input('enter the mivie you wish to add to the list saperated by a space:').split()
            if moviesr in favmovies:
                favmovies.remove(moviesr)
                print(f'the {moviesr} has been removed')

            else:
                print(f"The movie '{moviesr}' is not in the list.")

        elif action == 'display':
            if favmovies:
                for movie in favmovies:
                    print('the movies are:', favmovies)
            
            else:
                print('Your movie list is empty.')
       
        elif action == 'exit':
            print("Exiting the movie database. Goodbye!")
            break
        
        else: 
            print('input error, please try again')

#2. Write a program to find the second largest number in a list of numbers.
def second_largest():
    numbers = list(map(int, input('enter a list of numbers saperated by space:').split()))
    
    if len(numbers) < 2:
        print('List must contain at least two distinct numbers!')
    
    first = second = float('-inf')  # Initialize first and second largest

    for num in numbers:
        if num > first:
            second = first  # Update second largest
            first = num     # Update largest
        elif first > num > second:
            second = num    # Update second largest if it's between first and second

    return second if second != float('-inf') else "There is no second largest number."

#3. Generate a list of squares of numbers from 1 to 10 using list comprehension.


#4. Merge two lists provided by the user and remove duplicates from the resulting list.


#5. Write a program that counts the number of vowels in a given string.


#6. Create a program that asks the user to input 5 numbers and then prints the smallest number.


        
def main_menu():
    while True:
        print('\n...main menu...')
        print('1. movie database, add, remove, display ')
        print('2. second largest number ')
        print('3. ')
        print('4. ')
        print('5. ')
        print('0. Exit')

        choice = input('Choose an option: ').strip()

        if choice == '1':
            movie_db()
        
        elif choice == '2':
            second_largest()
    
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

# Start the program
main_menu()
