from parser import get_user_ratings, save_data_to_excel

def main():
    # Функция для запуска парсера
    user_id = 2054122

    user_ratings = get_user_ratings(user_id = 2054122)

    save_data_to_excel(user_ratings, 'user_ratings.xlsx')

    print("Данные сохранены в файл Excel.")

if __name__ == "__main__":
    main()