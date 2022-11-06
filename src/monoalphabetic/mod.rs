mod key;
mod preview;

use dioxus::prelude::{Element, rsx};


#[inline_props]
fn MonoAlphabetic(cx: Scope, text: String) -> Element {

    cx.render(rsx!(
        "{text}"
        
    ))
}