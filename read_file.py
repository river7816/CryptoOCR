import pickle

def save_list(lst, filename):
    with open(filename, 'wb') as f:
        pickle.dump(lst, f)

def load_list(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)



if __name__ == "__main__":
    base_asset_list = load_list('base_asset_list.pkl')
    print(base_asset_list)

