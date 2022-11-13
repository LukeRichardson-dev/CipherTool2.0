use dioxus::prelude::*;

mod vigenere;
use vigenere::Vinegere;

use crate::monoalphabetic::MonoAlphabetic;

mod monoalphabetic;
pub mod constants;

fn main() {
    dioxus::desktop::launch(app);
}

fn app(cx: Scope) -> Element {
    cx.render(rsx!(
        MonoAlphabetic {
            text: "BOVUSDSBDLFSMJLFTOVUT".to_string()
        }
    ))
}
