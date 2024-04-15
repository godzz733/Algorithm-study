use std::{cmp, io, vec};
use std::io::prelude::*;

fn read<T>(si: &mut T) -> String where T: Read {
    let mut s = String::new();
    si.read_to_string(&mut s).unwrap();
    s
}

fn next<T>(it: &mut std::str::SplitAsciiWhitespace) -> T where
    T: std::str::FromStr,
    <T as std::str::FromStr>::Err: std::fmt::Debug {
    it.next().unwrap().parse().unwrap()
}

struct Stack {
    v: Vec<i32>,
}
impl Stack {
    fn new() -> Stack {
        Stack {
            v: Vec::new()
        }
    }
    fn fn_1(st: &mut Stack, x: i32) {
        st.v.push(x);
    }

    fn fn_2(st: &mut Stack) -> i32{
        if st.v.is_empty() {
            return -1;
        } else {
            st.v.pop().unwrap()
        }
    }

    fn fn_3(st: &mut Stack) -> usize {
        st.v.len()
    }

    fn fn_4(st: &mut Stack) -> usize {
        if st.v.is_empty() {
            return 1;
        } else {
            0
        }
    }

    fn fn_5(st: &mut Stack) -> i32 {
        if st.v.is_empty() {
            return -1;
        } else {
            st.v[st.v.len() - 1]
        }
    }
}

fn main() {
    // 입력
    let mut si = io::BufReader::new(io::stdin().lock());
    let mut so = io::BufWriter::new(io::stdout().lock());
    let s = read(&mut si);
    let mut it = s.split_ascii_whitespace();

    let n: i32 = next(&mut it);
    let mut st = Stack::new();
    for _ in 0..n {
        let cmd: i32 = next(&mut it);
        if cmd == 1 {
            let x = next::<i32>(&mut it);
            Stack::fn_1(&mut st, x);
        } else if cmd == 2 {
            writeln!(so, "{}", Stack::fn_2(&mut st)).ok();
        } else if cmd == 3 {
            writeln!(so, "{}", Stack::fn_3(&mut st)).ok();
        } else if cmd == 4 {
            writeln!(so, "{}", Stack::fn_4(&mut st)).ok();
        } else if cmd == 5 {
            writeln!(so, "{}", Stack::fn_5(&mut st)).ok();
        }
    }
}