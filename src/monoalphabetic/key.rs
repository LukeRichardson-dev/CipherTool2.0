use dioxus::prelude::*;

#[derive(Debug, Clone)]
struct MonoalphabeticKey([u8; 26]);

#[inline_props]
pub fn KeyEditor(cx: Scope, monokey: UseRef<MonoalphabeticKey>) -> Element {
    let key = monokey.read().0;
    

    cx.render(rsx!(

    ))
}

fn 