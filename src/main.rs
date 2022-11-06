use dioxus::prelude::*;

mod vigenere;
use vigenere::Vinegere;

mod monoalphabetic;

fn main() {
    dioxus::desktop::launch(app);
}

fn app(cx: Scope) -> Element {
    cx.render(rsx!(
        Vinegere {
            text: "HelloWorldMyNameIsLuke".to_string()
        }
    ))
}
