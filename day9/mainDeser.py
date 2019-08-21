import pickle

if __name__ == '__main__':
        with open(r'/home/remvord/person', 'rb') as f:
            persons = pickle.load(f)
            for r in persons:
                print(r.ename, type(r))
