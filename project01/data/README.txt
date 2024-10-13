Summary
=======

This dataset (ml-25m) describes 5-star rating and free-text tagging activity from [MovieLens](http://movielens.org), a movie recommendation service. It contains 25000095 ratings and 1093360 tag applications across 62423 movies. These data were created by 162541 users between January 09, 1995 and November 21, 2019. This dataset was generated on November 21, 2019.

Users were selected at random for inclusion. All selected users had rated at least 20 movies. No demographic information is included. Each user is represented by an id, and no other information is provided.

The data are contained in the files `genome-scores.csv`, `genome-tags.csv`, `links.csv`, `movies.csv`, `ratings.csv` and `tags.csv`. More details about the contents and use of all these files follows.

This and other GroupLens data sets are publicly available for download at <http://grouplens.org/datasets/>.


Usage License
=============

Neither the University of Minnesota nor any of the researchers involved can guarantee the correctness of the data, its suitability for any particular purpose, or the validity of results based on the use of the data set. The data set may be used for any research purposes under the following conditions:

* The user may not state or imply any endorsement from the University of Minnesota or the GroupLens Research Group.
* The user must acknowledge the use of the data set in publications resulting from the use of the data set (see below for citation information).
* The user may not redistribute the data without separate permission.
* The user may not use this information for any commercial or revenue-bearing purposes without first obtaining permission from a faculty member of the GroupLens Research Project at the University of Minnesota.
* The executable software scripts are provided "as is" without warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The entire risk as to the quality and performance of them is with you. Should the program prove defective, you assume the cost of all necessary servicing, repair or correction.

In no event shall the University of Minnesota, its affiliates or employees be liable to you for any damages arising out of the use or inability to use these programs (including but not limited to loss of data or data being rendered inaccurate).

If you have any further questions or comments, please email <grouplens-info@umn.edu>


Citation
========

To acknowledge use of the dataset in publications, please cite the following paper:

> F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. <https://doi.org/10.1145/2827872>


Further Information About GroupLens
===================================

GroupLens is a research group in the Department of Computer Science and Engineering at the University of Minnesota. Since its inception in 1992, GroupLens's research projects have explored a variety of fields including:

* recommender systems
* online communities
* mobile and ubiquitious technologies
* digital libraries
* local geographic information systems

GroupLens Research operates a movie recommender based on collaborative filtering, MovieLens, which is the source of these data. We encourage you to visit <http://movielens.org> to try it out! If you have exciting ideas for experimental work to conduct on MovieLens, send us an email at <grouplens-info@cs.umn.edu> - we are always interested in working with external collaborators.


Content and Use of Files
========================

Verifying the Dataset Contents
------------------------------

We encourage you to verify that the dataset you have on your computer is identical to the ones hosted at [grouplens.org](http://grouplens.org).  This is an important step if you downloaded the dataset from a location other than [grouplens.org](http://grouplens.org), or if you wish to publish research results based on analysis of the MovieLens dataset.

We provide a [MD5 checksum](http://en.wikipedia.org/wiki/Md5sum) with the same name as the downloadable `.zip` file, but with a `.md5` file extension. To verify the dataset:

    # on linux
    md5sum ml-25m.zip; cat ml-25m.zip.md5

    # on OSX
    md5 ml-25m.zip; cat ml-25m.zip.md5

    # windows users can download a tool from Microsoft (or elsewhere) that verifies MD5 checksums

Check that the two lines of output contain the same hash value.


Formatting and Encoding
-----------------------

The dataset files are written as [comma-separated values](http://en.wikipedia.org/wiki/Comma-separated_values) files with a single header row. Columns that contain commas (`,`) are escaped using double-quotes (`"`). These files are encoded as UTF-8. If accented characters in movie titles or tag values (e.g. Misérables, Les (1995)) display incorrectly, make sure that any program reading the data, such as a text editor, terminal, or script, is configured for UTF-8.


User Ids
--------

MovieLens users were selected at random for inclusion. Their ids have been anonymized. User ids are consistent between `ratings.csv` and `tags.csv` (i.e., the same id refers to the same user across the two files).


Movie Ids
---------

Only movies with at least one rating or tag are included in the dataset. These movie ids are consistent with those used on the MovieLens web site (e.g., id `1` corresponds to the URL <https://movielens.org/movies/1>). Movie ids are consistent between `ratings.csv`, `tags.csv`, `movies.csv`, and `links.csv` (i.e., the same id refers to the same movie across these four data files).


Ratings Data File Structure (ratings.csv)
-----------------------------------------

All ratings are contained in the file `ratings.csv`. Each line of this file after the header row represents one rating of one movie by one user, and has the following format:

    userId,movieId,rating,timestamp

The lines within this file are ordered first by userId, then, within user, by movieId.

Ratings are made on a 5-star scale, with half-star increments (0.5 stars - 5.0 stars).

Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970.


Tags Data File Structure (tags.csv)
-----------------------------------

All tags are contained in the file `tags.csv`. Each line of this file after the header row represents one tag applied to one movie by one user, and has the following format:

    userId,movieId,tag,timestamp

The lines within this file are ordered first by userId, then, within user, by movieId.

Tags are user-generated metadata about movies. Each tag is typically a single word or short phrase. The meaning, value, and purpose of a particular tag is determined by each user.

Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970.


Movies Data File Structure (movies.csv)
---------------------------------------

Movie information is contained in the file `movies.csv`. Each line of this file after the header row represents one movie, and has the following format:

    movieId,title,genres

Movie titles are entered manually or imported from <https://www.themoviedb.org/>, and include the year of release in parentheses. Errors and inconsistencies may exist in these titles.

Genres are a pipe-separated list, and are selected from the following:

* Action
* Adventure
* Animation
* Children's
* Comedy
* Crime
* Documentary
* Drama
* Fantasy
* Film-Noir
* Horror
* Musical
* Mystery
* Romance
* Sci-Fi
* Thriller
* War
* Western
* (no genres listed)


Links Data File Structure (links.csv)
---------------------------------------

Identifiers that can be used to link to other sources of movie data are contained in the file `links.csv`. Each line of this file after the header row represents one movie, and has the following format:

    movieId,imdbId,tmdbId

movieId is an identifier for movies used by <https://movielens.org>. E.g., the movie Toy Story has the link <https://movielens.org/movies/1>.

imdbId is an identifier for movies used by <http://www.imdb.com>. E.g., the movie Toy Story has the link <http://www.imdb.com/title/tt0114709/>.

tmdbId is an identifier for movies used by <https://www.themoviedb.org>. E.g., the movie Toy Story has the link <https://www.themoviedb.org/movie/862>.

Use of the resources listed above is subject to the terms of each provider.


Tag Genome (genome-scores.csv and genome-tags.csv)
-------------------------------------------------

This data set includes a current copy of the Tag Genome.

[genome-paper]: http://files.grouplens.org/papers/tag_genome.pdf

The tag genome is a data structure that contains tag relevance scores for movies.  The structure is a dense matrix: each movie in the genome has a value for *every* tag in the genome.

As described in [this article][genome-paper], the tag genome encodes how strongly movies exhibit particular properties represented by tags (atmospheric, thought-provoking, realistic, etc.). The tag genome was computed using a machine learning algorithm on user-contributed content including tags, ratings, and textual reviews.

The genome is split into two files.  The file `genome-scores.csv` contains movie-tag relevance data in the following format:

    movieId,tagId,relevance

The second file, `genome-tags.csv`, provides the tag descriptions for the tag IDs in the genome file, in the following format:

    tagId,tag

The `tagId` values are generated when the data set is exported, so they may vary from version to version of the MovieLens data sets.

Please include the following citation if referencing tag genome data:

> Jesse Vig, Shilad Sen, and John Riedl. 2012. The Tag Genome: Encoding Community Knowledge to Support Novel Interaction. ACM Trans. Interact. Intell. Syst. 2, 3: 13:1–13:44. <https://doi.org/10.1145/2362394.2362395>


Cross-Validation
----------------

Prior versions of the MovieLens dataset included either pre-computed cross-folds or scripts to perform this computation. We no longer bundle either of these features with the dataset, since most modern toolkits provide this as a built-in feature. If you wish to learn about standard approaches to cross-fold computation in the context of recommender systems evaluation, see [LensKit](http://lenskit.org) for tools, documentation, and open-source code examples.










总结
========================
该数据集（ml-25m）描述了[MovieRens]的五星评级和免费文本标记活动(http://movielens.org)，一个电影推荐服务。它包含25000095个评级和1093360个标签应用程序，涉及62423部电影。这些数据由162541名用户在1995年1月9日至2019年11月21日期间创建。该数据集生成于2019年11月21日。
用户是随机选择的。所有被选中的用户都对至少20部电影进行了评分。不包括人口统计信息。每个用户都由一个id表示，并且不提供其他信息。
这些数据包含在文件“genome scores.csv”、“genome tags.csv”、“links.csv”、“movies.com”、“ratings.csv”和“tags.csv'中。以下是关于所有这些文件的内容和使用的更多详细信息。
此数据集和其他GroupLens数据集可在上公开下载<http://grouplens.org/datasets/>.


文件的内容和使用
========================

验证数据集内容
------------------------------
我们鼓励您验证您计算机上的数据集是否与[grouplens.org/上托管的数据集相同(http://grouplens.org).  如果您从[grouplens.org/]以外的位置下载数据集，这是一个重要的步骤(http://grouplens.org)，或者如果您希望发布基于MovieLens数据集分析的研究结果。
我们提供[MD5校验和](http://en.wikipedia.org/wiki/Md5sum)与可下载的“.zip”文件同名，但文件扩展名为“.md5”。要验证数据集，请执行以下操作：
#在linux上
md5sum ml-25m.zip；猫ml-25m.zip.md5
#在OSX上
md5 ml-25m.zip；猫ml-25m.zip.md5
#windows用户可以从Microsoft（或其他地方）下载一个验证MD5校验和的工具
检查两行输出是否包含相同的哈希值。

格式和编码
-----------------------
数据集文件被写成[逗号分隔的值](http://en.wikipedia.org/wiki/Comma-separated_values)具有单个标题行的文件。包含逗号（`，`）的列使用双引号（`“`）进行转义。这些文件编码为UTF-8。如果电影标题或标记值（例如Misérables，Les（1995））中的重音字符显示不正确，请确保任何读取数据的程序（如文本编辑器、终端或脚本）都配置为UTF-8。

用户ID
--------
MovieLens的用户是随机选择的。他们的身份证已被匿名化。用户id在“ratings.csv”和“tags.csv”之间是一致的（即，同一id指的是两个文件中的同一用户）。

电影ID
---------
只有具有至少一个分级或标签的电影才包括在数据集中。这些电影id与MovieLens网站上使用的id一致（例如，id“1”对应URL<https://movielens.org/movies/1>). 电影id在“ratings.csv”、“tags.csv”、“movies.csv”和“links.csv“之间是一致的（即，在这四个数据文件中，相同的id指的是同一部电影）。

评级数据文件结构（Ratings.csv）
-----------------------------------------
所有评级都包含在文件“ratings.csv”中。该文件标题行后的每一行代表一个用户对一部电影的一个评分，其格式如下：
userId，movieId，分级，时间戳

该文件中的行首先按userId排序，然后在user中按movieId排序。
评级以五星为单位，以半星为增量（0.5星-5.0星）。
时间戳表示自1970年1月1日协调世界时（UTC）午夜以来的秒数。

标记数据文件结构（Tags.csv）
-----------------------------------
所有标记都包含在文件“tags.csv”中。该文件头行之后的每一行表示一个用户应用于一部电影的一个标记，其格式如下：
userId，movieId，标记，时间戳

该文件中的行首先按userId排序，然后在user中按movieId排序。
标签是用户生成的关于电影的元数据。每个标签通常是一个单词或短语。特定标签的含义、价值和用途由每个用户决定。
时间戳表示自1970年1月1日协调世界时（UTC）午夜以来的秒数。

电影数据文件结构（Movies.csv）
---------------------------------------
电影信息包含在文件“movies.csv”中。该文件头行后的每一行表示一部电影，格式如下：
电影ID、标题、流派

电影标题是手动输入或从导入的<https://www.themoviedb.org/>，并在括号中包括发布年份。这些标题中可能存在错误和不一致之处。
流派是一个管道分隔的列表，可从以下列表中选择：
动作、冒险、动画、儿童、喜剧、犯罪、纪录片、戏剧、幻想、黑色电影、恐怖、音乐剧、神秘、浪漫、科幻、惊悚片、战争、西部片（未列出流派）

链接数据文件结构（Links.csv）
---------------------------------------
可用于链接到其他电影数据源的标识符包含在文件“links.csv”中。该文件头行后的每一行表示一部电影，格式如下：
movieId、imdbId、tmdbId

movieId是由使用的电影的标识符<https://movielens.org>. 例如，电影《玩具总动员》有链接<https://movielens.org/movies/1>.

imdbId是电影的标识符，由<http://www.imdb.com>. 例如，电影《玩具总动员》有链接<http://www.imdb.com/title/tt0114709/>.

tmdbId是电影的标识符，由<https://www.themoviedb.org>. 例如，电影《玩具总动员》有链接<https://www.themoviedb.org/movie/862>.
上述资源的使用受各供应商的条款约束。

标签基因组（Genome-scores.csv和基因组标签.csv）
---------------------------------------
该数据集包括标签基因组的当前副本。[基因组论文]：http://files.grouplens.org/papers/tag_genome.pdf

标签基因组是一种包含电影标签相关性分数的数据结构。该结构是一个密集的矩阵：基因组中的每个电影都有一个基因组中每个标签的值。

如[本文][基因组论文]所述，标签基因组编码电影表现出标签所代表的特定特性（大气、发人深省、现实等）的强度。标签基因组是使用机器学习算法对用户贡献的内容（包括标签、评级和文本评论）进行计算的。

基因组被分成两个文件。文件“genome scores.csv”包含以下格式的电影标签相关性数据：
movieId，标签Id，相关性

第二个文件“genome tags.csv”提供了基因组文件中标签ID的标签描述，格式如下：
tagId，标签

“tagId”值是在导出数据集时生成的，因此它们可能因MovieLens数据集的版本而异。



这段代码主要用于测试基于 CountMinSketch 的数据结构在处理数据时的准确性。下面是如何使用这段代码来测试准确性的方法：
1.**准备真实计数数据：**首先，准备一个包含真实计数的字典，其中键是电影的标识符，值是真实的计数。
python
Copy code
true_counts = {"movie1": 100, "movie2": 150, "movie3": 200}
1.**执行更新操作：**执行一系列更新操作，例如增加或减少电影的计数。这些操作模拟了真实环境中的数据更新。
python
Copy code
updates = ["movie1", "movie2", "movie3", "movie1", "movie2"]
1.**执行查询操作：**执行一系列查询操作，查找特定电影的计数。这些查询操作模拟了用户查询电影计数的情况。
python
Copy code
queries = ["movie1", "movie4", "movie3"]
1.**执行性能评估：**调用 evaluate_performance 函数来评估 CountMinSketch 的性能。该函数将返回一系列性能指标，包括构建时间、更新时间、查询时间、精度和空间占用。
python
Copy code
performance_metrics = evaluate_performance(true_counts, updates, queries, timestamp, initial_width, depth)
1.**查看结果：**查看返回的性能指标，特别关注准确性（精度）指标。该指标反映了 CountMinSketch 估算的计数与真实计数之间的差异程度。
