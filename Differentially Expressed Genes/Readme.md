
# Differential Gene Expression

## Part 1 - Finding Differentially Expressed Genes using R

### What is Gene Expression?

Gene Expression is the process by which the instruction in our DNA are converted into a functional product , such as a protein.

Gene expression is a tightly regulated process that allows a cell to respond to its changing environment.
It acts as both on /off switch to control when proteins are made and also a volume control that increases or decreases the amount of proteins made.

### What are differentially Expressed Genes?

A gene is declared differentially expressed if a difference or change observed in read counts or expression levels/index between two experimental conditions is statistically significant.

Differential gene expression is important to understand the biological differences between healthy and diseased states. Two common sources of differential gene expression data are microarray studies and the biomedical literature. We use fold change cutoff values and significance of p values to determine the level of gene expression.

### Visualising Differentially Expressed Genes:

1. Heat maps

A heat map is a data visualization technique that shows magnitude of a phenomenon as color in two dimensions. The variation in color may be by hue or intensity, giving obvious visual cues to the reader about how the phenomenon is clustered or varies over space.

![](https://github.com/Rahul-Ganesan/Bioinformatics-and-Biological-Systems/blob/0893f928d572e0cd0485d042f3a6269a7ad86c5f/Differentially%20Expressed%20Genes/R/One.png)

2. Volcano Plots

In statistics, a volcano plot is a type of scatter-plot that is used to quickly identify changes in large data sets composed of replicate data. It plots significance versus fold-change on the y and x axes, respectively. These plots are increasingly common in omic experiments such as genomics, proteomics, and metabolomics where one often has a list of many thousands of replicate data points between two conditions and one wishes to quickly identify the most meaningful changes. 

![](https://github.com/Rahul-Ganesan/Bioinformatics-and-Biological-Systems/blob/0893f928d572e0cd0485d042f3a6269a7ad86c5f/Differentially%20Expressed%20Genes/R/Two.png)

### Results

![](https://github.com/Rahul-Ganesan/Bioinformatics-and-Biological-Systems/blob/0893f928d572e0cd0485d042f3a6269a7ad86c5f/Differentially%20Expressed%20Genes/R/Four.png)

![](https://github.com/Rahul-Ganesan/Bioinformatics-and-Biological-Systems/blob/0893f928d572e0cd0485d042f3a6269a7ad86c5f/Differentially%20Expressed%20Genes/R/Five.png)

Top 500 genes and their Z score

![](https://github.com/Rahul-Ganesan/Bioinformatics-and-Biological-Systems/blob/0893f928d572e0cd0485d042f3a6269a7ad86c5f/Differentially%20Expressed%20Genes/R/Six.png)

VOOM Mean Variance Trend of Differentially Expressed Genes

![](https://github.com/Rahul-Ganesan/Bioinformatics-and-Biological-Systems/blob/0893f928d572e0cd0485d042f3a6269a7ad86c5f/Differentially%20Expressed%20Genes/R/Seven.png)

Comparing LogPCM and VOOM Transferred LogPCM

![](https://github.com/Rahul-Ganesan/Bioinformatics-and-Biological-Systems/blob/0893f928d572e0cd0485d042f3a6269a7ad86c5f/Differentially%20Expressed%20Genes/R/Eight.png)

Interactive Dashboard Showing MDS plot and its proportion in two separate graphs

## Part 2 - Network Construction of differentially expressed gene :

A differential network analysis compares individual networks from different populations, or groups, to identify group-specific connections. Differences in the topology of two networks may indicate differences in the underlying cellular activity. For example, the existence of differentially connected (DC) gene modules might indicate that various pathways have been rewired.

![Image depicting final network construction using differential expression](https://github.com/Rahul-Ganesan/Bioinformatics-and-Biological-Systems/blob/db858d2df41c002bf2fbf91dcb3bb5a81a35a370/Differentially%20Expressed%20Genes/One.png)

i)Networks inferred from gene expression data are called gene co-expression networks (GCN).

ii)These are undirected graphs with nodes representing genes and edges representing gene-gene associations.

iii)The topology of the inferred network is used to make predictions about the genes. 

iv)For example, a hub gene in the network may be a transcription factor that regulates its connected genes. Or, a connected component in the network might be a set of genes involved in a particular pathway or protein complex.

## Centrality Measure

i) The structural analysis of biological networks includes the ranking of the vertices based on the connection structure of a network.

ii) To support this study we discuss centrality measures which indicate the importance of vertices, demonstrate their applicability on a gene regulatory network. 

iii) We show that common centrality measures result in different valuations of the vertices and that novel measures tailored to specific biological investigations are useful for the analysis of biological networks, in particular gene regulatory networks.

### Local Based Method and Global Based Method

i) To calculate the score of a node within a network, a local rank method only considers the relationship between the node and its direct neighbours 
global method examines the relationship between the node and the entire network.

We have 11 node ranking methods to evaluate the importance in biological networking.

Local Based Methods

1. Degree method (Deg)
2. Maximum Neighborhood Component (MNC)
3. Density of Maximum Neighborhood Component (DMNC)
4. Maximal Clique Centrality (MCC)

Global Based Methods

1. Closeness (Clo)
2. EcCentricity (EC)
3. Radiality (Rad)
4. BottleNeck (BN)
5. Stress (Str)
6. Betweenness (BC)
7. Edge Percolated Component (EPC)

## String Enrichment Analysis

String Enrichment Analysis is a method to identify classes of genes and proteins that are over – represented in a large set of gene or protein , and may have an association with disease phenotypes. 

The method uses statistical approaches to identify significantly enriched or depleted groups of genes. 

Transcriptomics technologies and proteomics results often identify thousands of genes which are used for the analysis.

## Results

String Network Constructed from differentially expressed genes

![](https://github.com/Rahul-Ganesan/Bioinformatics-and-Biological-Systems/blob/f8c664f1cce509769173b7089c361c5d9a866f82/Differentially%20Expressed%20Genes/STRING%20network.png)

## Resources and Software Used

R Studio

[Cytoscape](https://cytoscape.org/)

[CytoHubba](https://bmcsystbiol.biomedcentral.com/articles/10.1186/1752-0509-8-S4-S11)

[Gene Ontology Term Enrichment Analysis](https://pubmed.ncbi.nlm.nih.gov/27780226/)

[Fold Change Analysis](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-13-S2-S11)

[Analysis of Gene Expression of humna breast milk](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8605299/)
