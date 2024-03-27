use std::process::exit;
use std::{io, vec};
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
    let arr = (0..n).map(|_|
    next::<usize>(&mut it)).collect::<Vec<usize>>();
    let mut dp = vec![vec![false; arr.len()]; arr.len()];

    for l in (0..n) {
        for start in (0..n-l) {
            let end = start + l;
            if start == end {
                dp[start][end] = true;
            }
            else if arr[start] == arr[end] {
                if start + 1 == end {
                    dp[start][end] = true;
                }
                else {
                    dp[start][end] = dp[start+1][end-1];
                }
            }
        }
    }
    for i in (0..next::<usize>(&mut it)) {
        let start = next::<usize>(&mut it) - 1;
        let end = next::<usize>(&mut it) - 1;
        if dp[start][end] {
            writeln!(so, "1").ok();
        }
        else {
            writeln!(so, "0").ok();
        }
    }
}