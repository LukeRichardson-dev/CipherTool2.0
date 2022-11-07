use dioxus::prelude::*;

mod vigenere;
use vigenere::Vinegere;

use crate::monoalphabetic::MonoAlphabetic;

mod monoalphabetic;

fn main() {
    dioxus::desktop::launch(app);
}

fn app(cx: Scope) -> Element {
    cx.render(rsx!(
        Vinegere {
            text: "ANUTRCRACKERLIKESNUTS".to_string()
        }
    ))
}
