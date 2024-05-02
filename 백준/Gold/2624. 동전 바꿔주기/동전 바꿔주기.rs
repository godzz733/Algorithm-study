use std::collections::HashMap;
use std::iter::Map;
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


fn main() {
    // 입력
    let mut si = io::BufReader::new(io::stdin().lock());
    let mut so = io::BufWriter::new(io::stdout().lock());
    let s = read(&mut si);
    let mut it = s.split_ascii_whitespace();

    let n = next::<usize>(&mut it);
    let m = next::<usize>(&mut it);
    let mut arr = Vec::new();
    for _ in 0..=n {
        arr.push(0);
    }
    arr[0] = 1;
    for _ in 0..m {
        let a = next::<usize>(&mut it);
        let b = next::<usize>(&mut it);
        for i in (1..=n).rev() {
            for j in 1..=b {
                if i < j * a {
                    break;
                }
                arr[i] += arr[i - j * a];
            }
        }
    }
    writeln!(so, "{}", arr[n]).ok();
}