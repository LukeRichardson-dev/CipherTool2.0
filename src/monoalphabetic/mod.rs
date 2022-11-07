mod key;
mod preview;

use dioxus::prelude::*;

use crate::monoalphabetic::key::KeyEditor;

use self::key::MonoalphabeticKey;

#[inline_props]
pub fn MonoAlphabetic(cx: Scope, text: String) -> Element {
    let monokeyref = use_ref(&cx, || MonoalphabeticKey([0u8; 26]));

    cx.render(rsx!(
        KeyEditor {
            monokey: monokeyref.clone()
        }
        "{text}"
    ))
}