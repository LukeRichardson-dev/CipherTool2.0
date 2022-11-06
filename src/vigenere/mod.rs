use dioxus::prelude::*;

mod key;
use key::*;

mod preview;
use preview::Preview;

#[derive(PartialEq, Props)]
pub struct VingereState {
    text: String,
}

pub fn Vinegere(cx: Scope<VingereState>) -> Element {
    let key = use_ref(&cx, || VinegereKey { key: vec![3, 4, 7, 2, 8] });

    key.read();
    cx.render(rsx! {
        div {
            KeyEditor {
                vinkey: key.clone()
            }
            Preview {
                txt: cx.props.text.clone(),
                vinkey: key.clone()
            }
            key.read().key.iter().map(|v| format!("{} ", v))
        }
    })
}