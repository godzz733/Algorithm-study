use std::io;
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

fn bisect(arr: &Vec<usize>, size: usize, target: usize) -> i32 {
    let mut st:i32 = 0;
    let mut end:i32 = size as i32;
    let mut res:i32 = -1;
    while st <= end {
        let mid = (st + end) >> 1;
        if arr[mid as usize] < target {
            st = mid + 1;
        } else {
            end = mid-1;
            res = mid as i32;
        }
    }
    if st == size as i32 {
        return -1;
    }
    res
}
fn main() {
    // 입력
    let mut si = io::BufReader::new(io::stdin().lock());
    let mut so = io::BufWriter::new(io::stdout().lock());
    let s = read(&mut si);
    let mut it = s.split_ascii_whitespace();
    
    let n = next::<usize>(&mut it);
    let mut arr:Vec<usize> = vec![0; n];
    let mut tem = (0..n).map(|_|
        next::<usize>(&mut it)).collect::<Vec<_>>();
    let mut size = 0;
    for x in tem {
        let mut t = bisect(&arr, size, x);
        if t == -1 {
            arr[size] = x;
            size += 1;
        } else {
            arr[t as usize] = x;
        }
    }
    writeln!(so,"{}", size).ok();
}