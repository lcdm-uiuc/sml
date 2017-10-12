from sklearn.model_selection import train_test_split

def handle_split(data, train):
    test = 1 - float(train)
    train_data, test_data = train_test_split(data,test_size=test)
    return train_data, test_data
