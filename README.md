# Snowflake-tool
Snowflake tool is a Python library that implements the Snowflake algorithm and is used to generate Snowflake ID.

The default Twitter format shown below.

```text
+------------------------------------------------------------------------------+
| 1 Bit Unused | 41 Bit Timestamp |  10 Bit Machine ID  |   12 Bit Sequence ID |
+------------------------------------------------------------------------------+
```
## Install

```shell
pip install snowflake-tool
```

## Usage

```python
from snowflake import Snowflake

gen = Snowflake(1)
for i in range(int(1e5)):
    print(next(gen))
```

Of course, you could also generate one id by generator:

```python
from snowflake import Snowflake

gen = Snowflake(1)
print(gen.generate())
```

### Reference:
1. [twitter-archive/snowflake: Snowflake is a network service for generating unique ID numbers at high scale with some simple guarantees. (github.com)](https://github.com/twitter-archive/snowflake)
2. [bwmarrin/snowflake: A simple to use Go (golang) package to generate or parse Twitter snowflake IDs (github.com)](https://github.com/bwmarrin/snowflake)
3. [Snowflake ID - Wikipedia](https://en.wikipedia.org/wiki/Snowflake_ID)