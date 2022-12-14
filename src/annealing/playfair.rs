use std::ops::Index;

use super::key::Key;

static DEFAULT: &'static [char; 25] = &['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];


pub fn backwards(text: &String, key: Key) -> String {

    let mut new = String::new();

    for l in text.as_bytes().to_vec().chunks(2) {
        let (a, b) = (l[0], l[1]);
        // println!("{} {}", a, b);

        let (aidx, bidx) = (
            key.0.iter().enumerate().find(|(_, &x)| x == a).unwrap().0, 
            key.0.iter().enumerate().find(|(_, &x)| x == b).unwrap().0
        );

        let ((nax, nay), (nbx, nby)): ((usize, usize), (usize, usize)) = playfair_transform(aidx, bidx, 4);
        let letters = String::from_utf8([key.0[nay * 5 + nax], key.0[nby * 5 + nbx]].to_vec()).unwrap();
        new = format!("{}{}", new, letters);
    }

    new
}

fn playfair_transform(aidx: usize, bidx: usize, offset: usize) -> ((usize, usize), (usize, usize)) {
    let (ay, ax, by, bx) = (aidx / 5, aidx % 5, bidx / 5, bidx % 5);

    if ax == bx {
        return (
            (ax, (ay + offset) % 5), 
            (bx, (by + offset) % 5)
        )
    }
    if ay == by {
        return (
            ((ax + offset) % 5, ay), 
            ((bx + offset) % 5, by)
        )
    }

    ((bx, ay), (ax, by))
}
        

