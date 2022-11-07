use dioxus::prelude::*;

#[derive(Debug, Clone)]
pub struct MonoalphabeticKey(pub [u8; 26]);

#[inline_props]
pub fn KeyEditor(cx: Scope, monokey: UseRef<MonoalphabeticKey>) -> Element {
    let key = monokey.read().0;

    cx.render(rsx!(
        table {
            tr {
                (0..26).map(|v| {
                    let chr = String::from_utf8(vec![v + 65]).unwrap();
                    rsx!(
                        "{chr}"
                    )
                })
            }
            (0..26).map(|v1| {
                rsx!(
                    tr {
                        (0..26).map(|v2| {
                            rsx!(
                                button {
                                    disabled: key[v2] == v1 ,
                                    "@"
                                }
                            )
                        })
                    }
                )
            })
        }
    ))
}
