mod key;
mod preview;

use dioxus::prelude::*;

use crate::monoalphabetic::{key::KeyEditor, preview::Preview};

use self::key::MonoalphabeticKey;

#[inline_props]
pub fn MonoAlphabetic(cx: Scope, text: String) -> Element {
    let monokeyref = use_ref(&cx, || MonoalphabeticKey([None; 26]));

    cx.render(rsx!(
        KeyEditor {
            monokey: monokeyref.clone()
        }
        Preview {
            plaintext: text.clone(),
            monokey: monokeyref.clone(),
        }
    ))
}