use dioxus::prelude::*;

mod vigenere;
use vigenere::Vinegere;

use crate::{monoalphabetic::MonoAlphabetic, constants::*};

mod monoalphabetic;
pub mod constants;

fn main() {
    dioxus::desktop::launch(app);
}

fn app(cx: Scope) -> Element {
    cx.render(rsx!(
        Vinegere {
            text: CHALLENGES_8_A.replace(" ", "").to_string()
        }
    ))
}
