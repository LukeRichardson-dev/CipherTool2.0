use super::{qgram::QGRAMS, key::Key, playfair::backwards};
use rand::random;


static TEMP: f64 = 10.0;
static STEP: f64 = 0.2;
static MAX_COUNT: usize = 10_000;

fn score_by_qgram(text: String) -> f64 {
    let mut s = 0f64;
    let bytes = text.as_bytes();
    for l in 0..(text.len() - 4) {
        let (oa, ob, oc, od) = (
            (bytes[l+0] - 65) as usize, 
            (bytes[l+1] - 65) as usize, 
            (bytes[l+2] - 65) as usize, 
            (bytes[l+3] - 65) as usize
        );
        s += QGRAMS[17576*oa+ 676*ob + 26*oc + od];
    }

    s
}

pub fn score_key(text: &String, key: Key) -> f64 {
    score_by_qgram(backwards(&text, key))
} 


pub fn crackPlayfair(text: String, key: Key) -> (Key, f64) {
    let mut best_key = key.clone();
    let mut max_key = key.clone();

    let mut best_score = score_key(&text, key);
    let mut max_score = best_score.clone();

    let mut T = TEMP;
    while T > 0.0 {
        println!("TOP SCORE --> {} KEY --> {:?}", best_score, String::from_utf8(best_key.0.to_vec()).unwrap());

        for _ in 0..MAX_COUNT {
            let test_key = max_key.child();
            let score = score_key(&text, test_key);

            let dF = score - max_score;

            if dF >= 0.0 {
                max_score = score;
                max_key = test_key;
            } else if T > 0.0 {
                let probability = (dF/T).exp();
                if probability > random::<f64>() {
                    max_score = score;
                    max_key = test_key;
                }
            }

            if max_score > best_score {
                best_score = max_score;
                best_key = max_key.clone();
            }
        }

        T -= STEP;
    }

    (best_key, best_score)
}

