import os
import pickle
import pprint
import sys
import argparse
from feature_extraction import extract_infos
from termcolor import colored
from sklearn.externals import joblib




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Detect malicious files')
    parser.add_argument('FILE', help='File to be tested')
    args = parser.parse_args()
    # Load classifier
    clf = joblib.load(os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'models/RandomForest.pkl'
    ))
    features = pickle.loads(open(os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'models/features.pkl'),
        'r').read()
    )

    data = extract_infos(args.FILE)
    print colored('\n\nExtracted features','white')
    print "*"*40
    pprint.pprint(data)
    print "*"*40
    print colored('Selected features','white')
    pprint.pprint(features)
    print "*"*40

    pe_features = map(lambda x:data[x], features)

    res = clf.predict([pe_features])[0]
    if res == 1:
        c = 'green'
    else:
        c = 'red'
    print('The file %s is %s' % (
        os.path.basename(sys.argv[1]),
        colored(['malicious', 'legitimate'][res],c))
    )


