import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))