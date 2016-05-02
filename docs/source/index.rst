##########################
Bitcoin: Some Nuts & Bolts
##########################

**PyData @ EyeQuant**

**April 2016, Berlin**

**sylvain@ascribe.io**



Thanks
======

.. rst-class:: build

* EyeQuant
* PyData
* To you, the audience


``whoami``
==========

.. rst-class:: build

* Sylvain Bellemare, `@sbellem <https://twitter.com/sbellem>`_
* Software engineer working at `ascribe <https://www.ascribe.io>`_
* Work on ``django/rest_framework`` -based API
* Previously worked with ``elasticsearch`` & ``django``



A few words about ascribe
=========================

.. rst-class:: build

* Circa 2014
* Intellectual Property on the Blockchain:
    * `SPOOL blockchain protocol`_
    * `SPOOL API`_
    * `ascribe.io <https://www.ascribe.io>`_
* Trace how images spread on the Internet over time:
    * `whereonthe.net <https://www.whereonthe.net/>`_
* A scalable blockchain database:
    * `BigchainDB <https://www.bigchaindb.com/>`__

+---------------------------------------+---------------------------------------+-----------------------------+
| .. image:: /_static/favicon-96x96.png | .. image:: /_static/whereonthenet.png | .. image:: /_static/bdb.png |
|                                       |     :scale: 20 %                      |                             |
+---------------------------------------+---------------------------------------+-----------------------------+


ascribe & white papers
=======================

.. rst-class:: build

* `Towards An Ownership Layer for the Internet`_
* `BigchainDB: A Scalable Blockchain Database <https://www.bigchaindb.com/whitepaper/>`__




ascribe & open source software
==============================

.. rst-class:: build

* `transactions`_: Bitcoin for humans
* `pyspool`_: Reference implementation of the SPOOL protocol
* `image-match`_: Quickly search over billions of images
* `bigchaindb <https://github.com/bigchaindb/bigchaindb>`_: A scalable blockchain database
* `cryptoconditions <https://pypi.python.org/pypi/cryptoconditions>`_: Python port of the `Interledger Protocol specifications <https://interledger.org/five-bells-condition/spec.html>`_

.. image:: /_static/python-powered-w.svg


Talk Outline
============

.. rst-class:: build

* Cryptographic primitives
* Bitcoin transactions
* Bitcoin blocks
* Bitcoin blockchain
* Bitcoin network and consensus
* Brief demo of ascribe


.. note::
 
    Brief mention of cryptographic primitives (hash functions & digital
    signatures) to simply point out their key role in bitcoin. But the talk
    assumes familiarity with each primitive.

    Brief mention of public keys, and how they are used to represent senders
    and receivers in bitcoin, through what is called bitcoin addresses. Again,
    assumption of familiarity with public key cryptography.
    
    Start with a bitcoin transaction, its data structure, validation via a
    script, but only cover the digital signature validation, and perhaps
    briefly mention that the script could be used for basic smart contracts.
    
    Look at how transactions are assembled into blocks. Show the data
    structure of a block. This will be an occasion to introduce Merkle trees,
    in the context of a block.

    Brief discussion of the role of the nonce, and other related fields, with
    respect to the hash puzzle that needs to be solved.

    Briefly show how the blocks are chained, to form the block chain.

    Bitcoin network -- perhaps terminate with a brief mention of the challenge
    of achieving consensus on what the block chain actually is since each node
    may have its own version.




Warnings
========

.. rst-class:: build

* **Some** Nuts & Bolts
* The problem of not understanding everything
* The problem of not knowing where to start


Richard Feynman: the feeling of confusion
=========================================

.. raw:: html

    <iframe width="420" height="315" src="https://www.youtube-nocookie.com/embed/lytxafTXg6c?rel=0" frameborder="0" allowfullscreen></iframe>

Feynman: 'Greek' vs 'Babylonian' mathematics
============================================

.. raw:: html

    <iframe width="420" height="315" src="https://www.youtube-nocookie.com/embed/YaUlqXRPMmY?rel=0" frameborder="0" allowfullscreen></iframe>


Bitcoin Origins
===============

.. rst-class:: build

    * Satoshi Nakamoto paper: `Bitcoin: A Peer-to-Peer Electronic Cash System <https://bitcoin.org/bitcoin.pdf>`_

.. figure:: /_static/the_hunt_for_satoshi_nakamoto.png

    `The Hunt For Satoshi Nakamoto <https://www.bitcoincomic.org/blog/hunt-for-satoshi-nakamoto-bitcoin-comic-gets-funded-available-soon/>`_ by `Alex Preukschat <https://www.bitcoincomic.org/blog/author/alexpreukschat/>`_ (usage granted by the author)

Bitcoin Key Points
==================

.. rst-class:: build

* Bitcoin is a decentralized payment system.
* Based on a public transaction ledger.
* The ledger is maintained by anonymous miners.
* Miners validate transactions, and generate blocks of transactions.
* For each block, miners include a coin creation transaction, for
  which they select the recipient of the newly minted coins.
* A valid block must include a nonce.
* To find a valid nonce, a miner must brute-force a hash inequality.
* Bitcoin mining with the block rewards & transaction fees create an incentive
  for miners to behave honestly, which in turn helps maintaining the integrity
  of the consensus chain aka "the" blockchain.
    
* Garay et al. `The Bitcoin Backbone Protocol: Analysis and Applications <https://eprint.iacr.org/2014/765.pdf>`_

    

Cryptographic Primitives
========================

.. rst-class:: build

* Hash functions
* Digital signatures

Secure Hash Algorithm - SHA-256
===============================

.. figure:: /_static/Merkle-damgard.png
    :scale: 140 %

|

`Merkle-Damgård hash construction <https://en.wikipedia.org/wiki/File:Merkle-damgard.png>`_
by `Matt Crypto <https://en.wikipedia.org/wiki/User:Matt_Crypto>`_ (public domain)

"SHA‐256 uses the Merkle‐Damgard transform to turn a fixed‐length
collision‐resistant compression function into a hash function that accepts
arbitrary‐length inputs. The input is “padded” so that its length is a multiple
of 512 bits." (`Narayanan et al.`_)
  

Davies–Meyer one-way compression function
=========================================

.. figure:: /_static/350px-Davies-Meyer_hash.svg

`Davies-Meyer hash construct <https://commons.wikimedia.org/wiki/File%3ADavies-Meyer_hash.svg>`_
that turns a block cipher into a one-way compression function that can be used
inside a hash function.

by `David Göthberg <https://commons.wikimedia.org/wiki/User:Davidgothberg>`_ (public domain)


Elliptic Curve Digital Signature Algorithm (ECDSA)
==================================================

.. figure:: /_static/Secp256k1.png
    :scale: 65 %

|

`secp256k1's elliptic curve y^2 = x^3 + 7 over the real numbers <https://en.bitcoin.it/wiki/File:Secp256k1.png>`_

by `Theymos <https://en.bitcoin.it/wiki/User:Theymos>`_ (public domain)


Alice & Bob
===========

.. figure:: /_static/alice-bob-tx.jpeg
    :scale: 16 %


Python & Bitcoin
================

* ``ecdsa``:
    * Pure Python ECDSA signature/verification. -- `@warner <https://github.com/warner>`_

* ``pycoin``:
    * Bitcoin and alt-coin utility library. -- `@richardkiss <https://github.com/richardkiss>`_

* ``pybitcointools``:
    * Common-sense Bitcoin-themed Python ECC library. -- `@vbuterin <https://github.com/vbuterin>`_
        
* ``python-bitcoinlib``:
    * Bitcoin library. -- `@petertodd <https://github.com/petertodd>`_

* ``transactions``:
    * Library to easily create, sign, and push bitcoin transactions. -- `@ascribe <https://github.com/ascribe>`_

    ---

.. code-block:: bash

    $ pip install ecdsa pycoin transactions     # for this talk

        

Alice: address creation with pycoin
===================================

.. code-block:: python

    >>> from pycoin.key.BIP32Node import BIP32Node
    
    >>> alice_master_secret = 'alice-super-duper-mega-top-secret'

    >>> alice_wallet = BIP32Node.from_master_secret(alice_master_secret, netcode='XTN')

    >>> alice = alice_wallet.bitcoin_address()

    >>> alice
    u'mp2YPeFdPufm515qWbmPXzSACxnMVdphnF'


    
Alice: view in blockchain explorer
==================================

.. figure:: /_static/alice.png
    
    blocktrail.com/tBTC/address/mp2YPeFdPufm515qWbmPXzSACxnMVdphnF


Bob: address creation with pycoin
=================================

.. code-block:: python

    >>> from pycoin.key.BIP32Node import BIP32Node
    
    >>> bob_wallet = BIP32Node.from_master_secret('bob-master-secret', netcode='XTN')

    >>> bob = bob_wallet.bitcoin_address()

    >>> bob
    u'n4mgh5qiBXj7Y3tLu4fqcPf5KubRVmR9Lr'


Bob: view in blockchain explorer
================================

.. figure:: /_static/bob.png
    
    blocktrail.com/tBTC/address/n4mgh5qiBXj7Y3tLu4fqcPf5KubRVmR9Lr
 


Alice & Bob -- view balances
============================

.. code-block:: python

    >>> from transactions.services.blockrservice import BitcoinBlockrService

    >>> blockr = BitcoinBlockrService(testnet=True)
    
    >>> alice, bob
     (u'mp2YPeFdPufm515qWbmPXzSACxnMVdphnF', u'n4mgh5qiBXj7Y3tLu4fqcPf5KubRVmR9Lr')

    >>> blockr.get_balance(alice)
    {u'address': u'mp2YPeFdPufm515qWbmPXzSACxnMVdphnF',
     u'balance': 1.22,
     u'balance_multisig': 0}

    >>> blockr.get_balance(bob)
    {u'address': u'n4mgh5qiBXj7Y3tLu4fqcPf5KubRVmR9Lr',
     u'balance': 0,
     u'balance_multisig': 0}


Alice sends 10000 satoshis to Bob
=================================

.. rst-class:: build

* Three steps by Alice:
    * Transaction creation
    * Transaction signature
    * Transaction broadcast

* Multiple steps required by the Bitcoin miners:
    * Transaction validation
    * Transaction relay to connected peers
    * Block generation (brute-foce hash inequality & group valid transactions)
    * Block broadcast
    * Block validation
    * Block chaining


Transaction Creation
====================

.. code-block:: python

    >>> from transactions import Transactions
    
    >>> transactions = Transactions(testnet=True)
    
    >>> transactions.create(alice, (bob, 10000))
    ('01000000014f2d34b5c41cfc34ffba6811280297cd3a45fdc4a982bd137219170e34d8a9950100000000'
     'ffffffff0210270000000000001976a914ff141b97e1bd38ccbafd72fdaed88b34d62337f588ac00e5b9'
     '01000000001976a9145d5988080ddb72dcb365755fbc1ea46bbee7628788ac00000000')

.. '01000000014f2d34b5c41cfc34ffba6811280297cd3a45fdc4a982bd137219170e34d8a9950100000000ffffffff0210270000000000001976a914ff141b97e1bd38ccbafd72fdaed88b34d62337f588ac00e5b901000000001976a9145d5988080ddb72dcb365755fbc1ea46bbee7628788ac00000000'


Transaction Signature
=====================

.. code-block:: python
    
    >>> from transactions import Transactions
    
    >>> transactions = Transactions(testnet=True)

    >>> ctx = transactions.create(alice, (bob, 10000))
    
    >>> stx = transactions.sign(ctx, alice_master_secret)
    ('01000000014f2d34b5c41cfc34ffba6811280297cd3a45fdc4a982bd137219170e34d8a995010000006b'
     '483045022100f52d33589ac95fda263d35a694dffcc9626d4c371a3140c020cf22956adc9e14022073c8'
     '33d254a13620ff0b4d9e0f8c52643962f1cdc7d684cbacf1a82692cee1ed01210256e335d68d2f4f9561'
     '985fb061a5c36ff9510b73005cf81e2f7a26e7bce0d8ceffffffff0210270000000000001976a914ff14'
     '1b97e1bd38ccbafd72fdaed88b34d62337f588ac00e5b901000000001976a9145d5988080ddb72dcb365'
     '755fbc1ea46bbee7628788ac00000000')

..  '01000000014f2d34b5c41cfc34ffba6811280297cd3a45fdc4a982bd137219170e34d8a995010000006b483045022100f52d33589ac95fda263d35a694dffcc9626d4c371a3140c020cf22956adc9e14022073c833d254a13620ff0b4d9e0f8c52643962f1cdc7d684cbacf1a82692cee1ed01210256e335d68d2f4f9561985fb061a5c36ff9510b73005cf81e2f7a26e7bce0d8ceffffffff0210270000000000001976a914ff141b97e1bd38ccbafd72fdaed88b34d62337f588ac00e5b901000000001976a9145d5988080ddb72dcb365755fbc1ea46bbee7628788ac00000000'


Transaction Broadcast
=====================

.. code-block:: python
     
    >>> from transactions import Transactions
    
    >>> transactions = Transactions(testnet=True)

    >>> ctx = transactions.create(alice, (bob, 10000))
    >>> stx = transactions.sign(ctx, alice_master_secret)
    
    >>> transactions.push(stx)
    2a77690c8d6d4eb8c49653ce8052fdea903328c095289eb389b6aad760ce6fcd


Decoded Signed Transaction
==========================

.. code-block:: python
    
    >>> from transactions import Transactions
    
    >>> transactions = Transactions(testnet=True)

    >>> ctx = transactions.create(alice, (bob, 10000))
    >>> stx = transactions.sign(ctx, alice_master_secret)
    
    >>> decoded_signed_tx = transactions.decode(stx)
    >>> decoded_signed_tx.keys()
    [u'statistics', u'tx']

    >>> decoded_signed_tx['statistics']
    {u'fee': u'0.00030000',
     u'vins_sum': u'0.29000000',
     u'vouts_sum': u'0.28970000'}


``decoded_signed_tx['tx']``
===========================

.. code-block:: python
    
    >>> decoded_signed_tx['tx'].keys()
    [u'vout', u'vin', u'txid', u'version', u'locktime', u'size']

    >>>  {k: v for k, v in decoded_signed_tx['tx'].iteritems()
          if k in ('txid', 'version', 'locktime', 'size')}
    {u'locktime': 0,
     u'size': 119,
     u'txid': u'f13611e756b4d6dcf167b26db33cbb9241bbc79971cf3331a1ba11c782fa5bdb',
     u'version': 1}


``decoded_signed_tx['tx']['vin']``
==================================

.. code-block:: python
    
    >>> decoded_signed_tx['tx']['vin']
    [{u'scriptSig': {u'asm': u'', u'hex': u''},
      u'sequence': 4294967295,
      u'txid': u'95a9d8340e17197213bd82a9c4fd453acd9702281168baff34fc1cc4b5342d4f',
      u'vout': 1}]


``decoded_signed_tx['tx']['vout']``
===================================

.. code-block:: python

    >>> decoded_signed_tx['tx']['vout']
    [{u'n': 0,
      u'scriptPubKey': {u'addresses': [u'n4mgh5qiBXj7Y3tLu4fqcPf5KubRVmR9Lr'],
       u'asm': ('OP_DUP OP_HASH160 ff141b97e1bd38ccbafd72fdaed88b34d62337f5'
                 ' OP_EQUALVERIFY OP_CHECKSIaG'),
       u'hex': u'76a914ff141b97e1bd38ccbafd72fdaed88b34d62337f588ac',
       u'reqSigs': 1,
       u'type': u'pubkeyhash'},
      u'value': 0.0001},
     {u'n': 1,
      u'scriptPubKey': {u'addresses': [u'mp2YPeFdPufm515qWbmPXzSACxnMVdphnF'],
       u'asm': ('OP_DUP OP_HASH160 5d5988080ddb72dcb365755fbc1ea46bbee76287'
                ' OP_EQUALVERIFY OP_CHECKSIG'),
       u'hex': u'76a9145d5988080ddb72dcb365755fbc1ea46bbee7628788ac',
       u'reqSigs': 1,
       u'type': u'pubkeyhash'},
      u'value': 0.2896}]




Get Transaction
===============

.. code-block:: python

    >>> from transactions import Transactions
    
    >>> transactions = Transactions(testnet=True)

    >>> ctx = transactions.create(alice, (bob, 10000))
    >>> stx = transactions.sign(ctx, alice_master_secret)
    >>> htx = transactions.push(stx)

    >>> transactions.get(htx, raw=True)
    {u'block': 787057,
     u'confirmations': 12,
     u'days_destroyed': u'0.10',
     u'extras': None,
     u'fee': u'0.00030000',
     u'is_coinbased': 0,
     u'is_unconfirmed': False,
     u'time_utc': u'2016-04-19T21:06:02Z',
     u'trade': {u'vins': [{u'address': u'mp2YPeFdPufm515qWbmPXzSACxnMVdphnF',
     ...
     ...



Bitcoin Block
=============

.. code-block:: python
 
    >>> tx = transactions.get(htx, raw=True)
    >>> block_height = tx['block']
    >>> transactions.get_block_raw(block_height)  
    {u'bits': u'1a072a74',
     u'chainwork': u'00000000000000000000000000000000000000000000000a1ef0e0907356e3b0',
     u'confirmations': 15,
     u'difficulty': 2341243.6662834,
     u'hash': u'00000000000003970a9fdd3f774995320c6eb729b01065fd86e210336b4022f3',
     u'height': 787057,
     u'mediantime': 1461096791,
     u'merkleroot': u'ba0393edef4e3eb899875df3f33332782203cad1da7ccb44ebcc9afb6c8ad755',
     u'nextblockhash': u'000000000003928b51f40754c294e39a6e4e32960ea7573f387eb1c9fe267932',
     u'nonce': 1554583068,
     u'previousblockhash': u'00000000000002bf692db2544bd4dec305f3c7977c8fae9993929503ed881626',
     u'size': 7705,
     u'time': 1461099962,
     u'tx': [u'dd34715e37f7335b43ef7facfd8af6473c68cda9c7757067614de55536b487f8',
             u'2a77690c8d6d4eb8c49653ce8052fdea903328c095289eb389b6aad760ce6fcd',
             u'f7314541e97547529a11ad5f6404f389770205f6569226fa1e69dae1c48d078e',
             ...
             ]
    u'version': 4}


Merkle Root
===========

.. code-block:: python
 
    >>> transactions.get_block_raw(787057)    
    {u'hash': u'00000000000003970a9fdd3f774995320c6eb729b01065fd86e210336b4022f3',
     u'merkleroot': u'ba0393edef4e3eb899875df3f33332782203cad1da7ccb44ebcc9afb6c8ad755',
     u'tx': [u'dd34715e37f7335b43ef7facfd8af6473c68cda9c7757067614de55536b487f8',
             u'2a77690c8d6d4eb8c49653ce8052fdea903328c095289eb389b6aad760ce6fcd',
             u'f7314541e97547529a11ad5f6404f389770205f6569226fa1e69dae1c48d078e',
             ...
             ]
    u'version': 4}

Merkle Tree (Hash Tree)
=======================

.. figure:: /_static/hashtree.png

    `Diagram of a binary hash tree <https://commons.wikimedia.org/wiki/File%3AHash_Tree.svg>`_
    by `Azaghal <https://commons.wikimedia.org/wiki/User:Azaghal>`_
    licensed under `CC0 1.0 <https://creativecommons.org/publicdomain/zero/1.0/deed.en>`_
   

Merkle Tree (Hash Tree)
=======================

.. figure:: /_static/Hashtreehashchainjux.png

    `8 leaf node hash tree & hash chain juxtaposition <https://en.wikipedia.org/wiki/File:Hashtreehashchainjux.png>`_ by `guardtime.com <https://commons.wikimedia.org/w/index.php?title=User:Iryanb&action=edit&redlink=1>`_
    
    licensed under `CC BY-SA 3.0`_


Computing the Merkle Root
=========================

.. code-block:: python
    
    import binascii
    import hashlib
    
    def merkleroot(hashes):
        """
        hashes: reversed binary form of transactions hashes
        returns: merkle root in hexadecimal form
        """
        if len(hashes) == 1:
            return binascii.hexlify(bytearray(reversed(hashes[0])))
        if len(hashes) % 2 == 1:
            hashes.append(hashes[-1])
        parent_hashes = []
        for i in range(0, len(hashes)-1, 2):
            first_round_hash = hashlib.sha256(hashes[i] + hashes[i+1]).digest()
            second_round_hash = hashlib.sha256(first_round_hash).digest()
            parent_hashes.append(second_round_hash)
        return merkleroot(parent_hashes)


Computing the Merkle Root
=========================

.. code-block:: python
    
    >>> block = transactions.get_block_raw(787057)
    >>> block['merkleroot']
    'ba0393edef4e3eb899875df3f33332782203cad1da7ccb44ebcc9afb6c8ad755'
    >>> hashes = [binascii.unhexlify(h)[::-1] for h in block['tx']]  
    >>> merkleroot(hashes)
    'ba0393edef4e3eb899875df3f33332782203cad1da7ccb44ebcc9afb6c8ad755'
    >>> merkleroot(hashes) == block['merkleroot']
    True

Bitcoin Blockchain
==================

.. code-block:: python
 
    >>> transactions.get_block_raw(787057)    
    {u'hash': u'00000000000003970a9fdd3f774995320c6eb729b01065fd86e210336b4022f3',
     u'merkleroot': u'ba0393edef4e3eb899875df3f33332782203cad1da7ccb44ebcc9afb6c8ad755',
     u'nextblockhash': u'000000000003928b51f40754c294e39a6e4e32960ea7573f387eb1c9fe267932',
     u'nonce': 1554583068,
     u'previousblockhash': u'00000000000002bf692db2544bd4dec305f3c7977c8fae9993929503ed881626',
     ...
     }


Hash Chain
==========

.. graphviz::

    digraph R {
        graph [
            fontname = "Helvetica-Oblique",
            size = "10!,10!",
            rankdir=LR
        ]
        node [
            style="rounded,filled",
            fillcolor="green"
        ]
        node1 [
            shape=Mrecord,
            label="hash(data-1) | data-1 | <p1> pointer",
        ]
        node2 [
            shape=record,
            label="<h2> hash(data-2) | <d2> data-2 | <p2> pointer"
        ]
        node3 [
            shape=record,
            label="<h3> hash(data-3) | <d3> data-3 | signature"
        ]
        node1:p1 -> node2:h2
        node2:p2 -> node3:h3
    }




Hash Tree Chain
===============

.. graphviz::

    digraph R {
        graph [
            fontname = "Helvetica-Oblique",
            size = "10!,10!",
            rankdir=LR
        ]
        node [
            style="rounded,filled",
            fillcolor="green"
        ]
        node1 [
            shape=record,
            label="<h1> hash:0 | nonce | difficulty | <d1> merkleroot | <n1> nextblockhash:4 | previousblockhash",
            fillcolor="yellow"
        ]
        node2 [
            shape=record,
            label="<h2> hash:4 | nonce | difficulty | <d2> mekleroot | <n2> nextblockhash:2 | <p2> previousblockhash:0"
        ]
        node3 [
            shape=record,
            label="<h3> hash:2 | nonce | difficulty | <d3> merkleroot | <n3> nextblockhash:7 | <p3> previousblockhash:4"
        ]
        node4 [
            shape=record,
            label="<h4> hash:7 | nonce | difficulty | merkleroot | <n4> nextblockhash:6 | <p4> previousblockhash:2"
        ]
        node1:n1 -> node2:h2
        node2:p2 -> node1:h1
        node2:n2 -> node3:h3
        node3:p3 -> node2:h2
        node3:n3 -> node4:h4
        node4:p4 -> node3:h3
    }


Genesis Block
=============

.. code-block:: python

    mainnet = Transactions()

    mainnet.get_block_raw('first')
    {u'bits': u'1d00ffff',
     u'chainwork': u'0000000000000000000000000000000000000000000000000000000200020002',
     u'confirmations': 408054,
     u'difficulty': 1,
     u'hash': u'00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048',
     u'height': 1,
     u'mediantime': 1231469665,
     u'merkleroot': u'0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098',
     u'nextblockhash': u'000000006a625f06636b8bb6ac7b960a8d03705d1ace08b1a19da3fdcc99ddbd',
     u'nonce': 2573394689,
     u'previousblockhash': u'000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f',
     u'size': 215,
     u'time': 1231469665,
     u'tx': [u'0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098'],
     u'version': 1}


Double Spending Attack
======================

.. figure:: /_static/double-spend.jpeg
    :scale: 16 %


Bitcoin Network & Consensus
===========================

.. rst-class:: build

* Peer-to-peer network
* Distributed consensus challenges
* Mining
* Hash puzzles
* Block rewards
* Transaction fees




The ascribe stack
=================

.. image:: /_static/ascribe-stack.jpg
    :scale: 75 %
    :align: center
    
Spring Time: decentralization efforts
=====================================

.. rst-class:: build

* `bigchaindb <https://github.com/bigchaindb/bigchaindb>`__: The scalable blockchain database
* `eris industries`_:  The Smart Contract Application Platform
* `ethereum`_: Blockchain App Platform
* `ipfs`_: InterPlanetary File System
* `tendermint`_: Consensus engine / TMSP (socket protocol)
* etc


Decentralized Stack
===================

.. figure:: /_static/future-stack
    :scale: 75 %


Creating a Bitcoin Address (1)
==============================

.. code-block:: python

    import hashlib

    from ecdsa import SigningKey, SECP256k1
    from pycoin.encoding import b2a_base58

    # generate a private ECDSA key (signing key)
    priv_key = '18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725'
    signing_key = SigningKey.from_string(priv_key.decode('hex'), curve=SECP256k1)

    # get the corressponding public (verifying) key
    verifying_key = signing_key.verifying_key

    # prefix with 1 byte 0x04
    pub_key = '\04' + verifying_key.to_string()

    # hash it using SHA-256
    sha256_of_pubkey = hashlib.sha256(pub_key).digest()


Creating a Bitcoin Address (2)
==============================

.. code-block:: python
    
    # perform a second round of hashing, using RIPEMD-160
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_of_pubkey)
    ripemd160_of_sha256_of_pubkey = ripemd160.digest()

    # prefix resulting with version byte (0x00 for mainnet)
    versioned_ripemd160 = '\00' + ripemd160_of_sha256_of_pubkey                                                                  
    
    # perform two more round of hashing with SHA-256
    sha256_of_versioned_ripemd = hashlib.sha256(versioned_ripemd160).digest()
    sha256_of_sha256_of_ripemd = hashlib.sha256(sha256_of_versioned_ripemd).digest()



Creating a Bitcoin Address (3)
==============================

.. code-block:: python
    
    # address checksum: first 4 bytes of last hash
    checksum = sha256_of_sha256_of_ripemd[:4]
    
    # 25-byte binary bitcoin address
    twenty_five_btc_addr = versioned_ripemd160 + checksum

    # convert byte string into a base58 string using Base58Check encoding
    b2a_base58(twenty_five_btc_addr)
    u'16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM'



Resources (1)
=============

.. rst-class:: build

* Original paper:
    * `Bitcoin: A Peer-to-Peer Electronic Cash System <https://bitcoin.org/bitcoin.pdf>`_ by Satoshi Nakamoto

* https://bitcoin.org/en/developer-documentation

* `Bitcoin book by Andreas M. Antonopoulos <https://github.com/bitcoinbook/bitcoinbook>`_

* Coursera: https://www.coursera.org/course/bitcointech
    * book: `Bitcoin and Cryptocurrency Technologies`_ by *Narayan et al.*

* In depth:
    * `The Bitcoin Backbone Protocol: Analysis and Applications <https://eprint.iacr.org/2014/765.pdf>`_ by Garay et al. 

* ascribe white papers:
    * `Towards An Ownership Layer for the Internet`_ by McConaghy & Holtzman
    * `BigchainDB: A Scalable Blockchain Database <https://www.bigchaindb.com/whitepaper/>`_ by McConaghy et al. 


Resources (2)
=============

* Python libraries:
    * `ecdsa`_
    * `pycoin`_, `pybitcointools`_, `python-bitcoinlib`_
    * `transactions`_, `pyspool`_

* Bitcoin addresses:
    * https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses
    * http://www.righto.com/2014/02/bitcoins-hard-way-using-raw-bitcoin.html

* Blockchain Explorers
    * http://blockr.io/
    * https://blockchain.info/
    * https://blockexplorer.com/
    * https://www.blocktrail.com/BTC


.. _Bitcoin and Cryptocurrency Technologies: https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf
.. _Narayanan et al.: https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf
.. _Arvind Narayanan: http://randomwalker.info/
.. _Joseph Bonneau: http://jbonneau.com/
.. _Edward Felten: https://www.cs.princeton.edu/~felten/
.. _Andrew Miller: https://cs.umd.edu/~amiller/
.. _Steven Goldfeder: https://www.cs.princeton.edu/~stevenag/
.. _Jeremy Clark: http://users.encs.concordia.ca/~clark/

.. _hard: https://en.wikipedia.org/wiki/Security_of_cryptographic_hash_functions#The_meaning_of_.22hard.22
.. _Descriptions of SHA-256, SHA-384, and SHA-512:  https://web.archive.org/web/20130526224224/http://csrc.nist.gov/groups/STM/cavp/documents/shs/sha256-384-512.pdf
.. _merkle tree: https://en.wikipedia.org/wiki/Merkle_tree
.. _merkle trees: https://en.wikipedia.org/wiki/Merkle_tree
.. _ralph merkle: https://en.wikipedia.org/wiki/Ralph_Merkle
.. _ecdsa: https://github.com/warner/python-ecdsa
.. _secp256k1: https://en.bitcoin.it/wiki/Secp256k1

.. _SPOOL API: https://www.ascribe.io/docs/
.. _SPOOL blockchain protocol: https://github.com/ascribe/spool
.. _eris industries: https://erisindustries.com/
.. _ethereum: https://www.ethereum.org/
.. _ipfs: https://ipfs.io/
.. _tendermint: http://tendermint.com/
.. _tmsp: https://github.com/tendermint/tmsp

.. _Towards An Ownership Layer for the Internet: https://d1qjsxua1o9x03.cloudfront.net/live/trent@ascribe.io/ascribe%20whitepaper%2020150624/digitalwork/ascribe%20whitepaper%2020150624.pdf
.. _transactions: https://github.com/ascribe/transactions
.. _pyspool: https://github.com/ascribe/pyspool
.. _image-match: https://github.com/ascribe/image-match

.. _pycoin: https://github.com/richardkiss/pycoin
.. _pybitcointools: https://github.com/vbuterin/pybitcointools
.. _python-bitcoinlib: https://github.com/petertodd/python-bitcoinlib

.. _CC BY-SA 3.0: https://creativecommons.org/licenses/by-sa/3.0/deed.en
