function tribonacci(signature, count = 5) {
  if (!signature || count  < 1) return []

  for (let i = 0; i < count ; i++) {
    const lastThree = signature.slice(-3);
    let sumLastThree = 0;

    lastThree.map((n) =>
      sumLastThree += n
    )

    signature.push(sumLastThree);
  }

  console.log(signature)
  return signature;
}

// tribonacci([1,1,1], 10)