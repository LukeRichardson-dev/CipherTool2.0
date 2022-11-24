use dioxus::prelude::*;

#[derive(Clone, PartialEq)]
pub struct VinegereKey {
    pub key: Vec<u8>,
}


#[inline_props]
pub fn KeyEditor(cx: Scope, vinkey: UseRef<VinegereKey>) -> Element {

    cx.render(rsx!(
        vinkey.read().key.iter().enumerate().map(|(idx, v)| {
            let l = String::from_utf8(vec![(26 - *v) % 26 + 65]).unwrap();
            rsx!(
                div { 
                    button {
                        onclick: move |_| {
                            vinkey.write().key[idx] += 25;
                            vinkey.write().key[idx] %= 26;
                        },
                        "-"
                    },
                    "{l}",
                    button {
                        onclick: move |_| {
                            vinkey.write().key[idx] += 1;
                            vinkey.write().key[idx] %= 26;
                        },
                        "+"
                    },
                }
            )
        } 
    )
    ))
}