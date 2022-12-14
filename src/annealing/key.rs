use dioxus::prelude::dioxus_elements::u;
use rand::prelude::*;

type KeyType = [u8; 25];

#[derive(Clone, Copy, Debug)]
pub struct Key(pub KeyType);

impl Key {
    pub fn new(key: KeyType) -> Self {
        Self(key)
    }

    pub fn default() -> Self{
        Self([65, 66, 67, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90])
    }

    pub fn child(&self) -> Self {
        let roll = random::<u32>() % 50;

        match roll {
            0 => Key::swap_cols(&self),
            1 => Key::swap_rows(&self),
            2 => {
                let mut n = self.0.clone();
                n.reverse();
                Self(n)
            }
            _ => Key::swap(&self)
        }
    }

    fn swap(&self) -> Self {
        let r1: usize = random::<usize>() % 25;
        let r2: usize = random::<usize>() % 25;

        let mut new = self.0.clone();
        let t = new[r1];
        new[r1] = new[r2];
        new[r2] = t;

        Self(new)
    }

    fn swap_rows(&self) -> Self {
        let mut nkey = self.0.clone();
        let i = random::<usize>() % 5;
        let j = random::<usize>() % 5;

        for k in 0..5 {
            let t = nkey[i*5 + k];
            nkey[i*5 + k] = nkey[j*5 + k];
            nkey[j*5 + k] = t;
        }

        Self(nkey)
    }

    fn swap_cols(&self) -> Self {
        let mut nkey = self.0.clone();
        let i = random::<usize>() % 5;
        let j = random::<usize>() % 5;

        for k in 0..5 {
            let t = nkey[k*5 + i];
            nkey[k*5 + i] = nkey[k*5 + j];
            nkey[k*5 + j] = t;
        }

        Self(nkey)
    }
}