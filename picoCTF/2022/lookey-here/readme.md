Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.
Download the data [here](https://artifacts.picoctf.net/c/294/anthem.flag.txt).


## solution

```bash
cat anthem.flag.txt | grep -o "picoCTF{.*}"
```