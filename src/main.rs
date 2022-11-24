use dioxus::prelude::*;

mod vigenere;
use vigenere::Vinegere;

use crate::{monoalphabetic::MonoAlphabetic, constants::{CHALLENGES_6_B, CHALLENGES_7_A, CHALLENGES_7_B}};

mod monoalphabetic;
pub mod constants;

fn main() {
    dioxus::desktop::launch(app);
}

fn app(cx: Scope) -> Element {
    cx.render(rsx!(
        Vinegere {
            text: CHALLENGES_7_B.replace(" ", "").to_string()
        }
    ))
}
