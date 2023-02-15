#include "TSP.hpp"

#include <algorithm>
#include <stack>
#include <string>
#include <optional>

std::ostream& operator<<(std::ostream& os, const CostMatrix& cm) {
    for (std::size_t r = 0; r < cm.size(); ++r) {
        for (std::size_t c = 0; c < cm.size(); ++c) {
            const auto& elem = cm[r][c];
            os << (is_inf(elem) ? "INF" : std::to_string(elem)) << " ";
        }
        os << "\n";
    }
    os << std::endl;

    return os;
}

/* PART 1 */

/**
 * Create path from unsorted path and last 2x2 cost matrix.
 * @return The vector of consecutive vertex.
 */
path_t StageState::get_path() {

     for (size_t i = 0; i < matrix_.size(); i++)
     {
         for (size_t j = 0; j < matrix_.size(); j++)
         {
          if (matrix_[i][j] != INF)
              unsorted_path_.push_back(vertex_t{i, j});
         }
     }

    std::vector<size_t> vertexToIndex(matrix_.size(), INF);
    for (size_t i = 0; i < unsorted_path_.size(); i++)
        vertexToIndex[unsorted_path_[i].row] = i;

    path_t finalPath = {1};

    size_t currentVertex = 0;
    while (finalPath.size() < matrix_.size())
    {
        size_t nextIndex = vertexToIndex[currentVertex];
        currentVertex = unsorted_path_[nextIndex].col;
        finalPath.push_back(currentVertex + 1);
    }

    return finalPath;
}

/**
 * Get minimum values from each row and returns them.
 * @return Vector of minimum values in row.
 */
std::vector<cost_t> CostMatrix::get_min_values_in_rows() const {
    
    std::vector<cost_t> minValues;

     for (size_t i = 0; i < matrix_.size(); i++)
     {
         cost_t minCost = INF;
         for (size_t j = 0; j < matrix_.size(); j++)
         {
             if (matrix_[i][j] < minCost)
                 minCost = matrix_[i][j];
         }
         minValues.push_back(minCost);
     }

    return minValues;
}

/**
 * Reduce rows so that in each row at least one zero value is present.
 * @return Sum of values reduced in rows.
 */
cost_t CostMatrix::reduce_rows() {
    
    std::vector<cost_t> minInRows = get_min_values_in_rows();

     for (size_t i = 0; i < matrix_.size(); i++)
     {
         for (size_t j = 0; j < matrix_.size(); j++)
         {
             if (minInRows[i] != INF && matrix_[i][j] != INF)
                 matrix_[i][j] -= minInRows[i];
         }
     }

    cost_t totalCost = 0;
    for (cost_t min : minInRows)
        if (min != INF)
            totalCost += min;
    return totalCost;
}

/**
 * Get minimum values from each column and returns them.
 * @return Vector of minimum values in columns.
 */
std::vector<cost_t> CostMatrix::get_min_values_in_cols() const {
    
    std::vector<cost_t> minValues;

     for (size_t i = 0; i < matrix_.size(); i++)
     {
         cost_t minCost = INF;
         for (size_t j = 0; j < matrix_.size(); j++)
         {
             if (matrix_[j][i] < minCost)
                 minCost = matrix_[j][i];
         }
         minValues.push_back(minCost);
     }


    return minValues;
}

/**
 * Reduces rows so that in each column at least one zero value is present.
 * @return Sum of values reduced in columns.
 */
cost_t CostMatrix::reduce_cols() {
    std::vector<cost_t> minInCols = get_min_values_in_cols();

     for (size_t i = 0; i < matrix_.size(); i++)
     {
         for (size_t j = 0; j < matrix_.size(); j++)
         {
             if (minInCols[i] != INF && matrix_[j][i] != INF)
                 matrix_[j][i] -= minInCols[i];
         }
     }

    cost_t totalCost = 0;
    for (cost_t min : minInCols)
        if (min != INF)
            totalCost += min;
    return totalCost;
}

/**
 * Get the cost of not visiting the vertex_t (@see: get_new_vertex())
 * @param row
 * @param col
 * @return The sum of minimal values in row and col, excluding the intersection value.
 */
cost_t CostMatrix::get_vertex_cost(std::size_t row, std::size_t col) const {
    cost_t minRow = INF, minCol = INF;
    for (size_t i = 0; i < size(); i++)
    {
        if (i != col && matrix_[row][i] < minRow)
            minRow = matrix_[row][i];

        if (i != row && matrix_[i][col] < minCol)
            minCol = matrix_[i][col];
    }
    return minRow == INF || minCol == INF ? INF : minRow + minCol;
}

/* PART 2 */

/**
 * Choose next vertex to visit:
 * - Look for vertex_t (pair row and column) with value 0 in the current cost matrix.
 * - Get the vertex_t cost (calls get_vertex_cost()).
 * - Choose the vertex_t with maximum cost and returns it.
 * @param cm
 * @return The coordinates of the next vertex.
 */
NewVertex StageState::choose_new_vertex() {

     vertex_t bestVertex;
     cost_t   bestCost = 0;
     for (size_t row = 0; row < matrix_.size(); row++)
         for (size_t col = 0; col < matrix_.size(); col++)
             if (matrix_[row][col] == 0)
             {
                 cost_t currentCost = matrix_.get_vertex_cost(row, col);
                 if (currentCost > bestCost)
                 {
                     bestCost = currentCost;
                     bestVertex = {row, col};
                 }
             }

    return NewVertex{bestVertex, bestCost};
}

/**
 * Update the cost matrix with the new vertex.
 * @param new_vertex
 */
void StageState::update_cost_matrix(vertex_t new_vertex) {
    
    size_t row = new_vertex.row;
    size_t col = new_vertex.col;

    for (size_t i = 0; i < matrix_.size(); i++)
    {
        matrix_[row][i] = INF;
        matrix_[i][col] = INF;
    }

    matrix_[col][row] = INF;

    std::vector<size_t> forwardIndices(matrix_.size(), INF);
    std::vector<size_t> backwardIndices(matrix_.size(), INF);
    for (size_t i = 0; i < unsorted_path_.size(); i++)
    {
        forwardIndices[unsorted_path_[i].row] = i;
        backwardIndices[unsorted_path_[i].col] = i;
    }

    size_t startVertex = row;
    size_t endVertex = col;

    bool startReached = false;
    bool endReached = false;
    while (!endReached)
    {
        size_t nextIndex = forwardIndices[endVertex];
        if (nextIndex != INF)
            endVertex = unsorted_path_[nextIndex].col;
        else 
            endReached = true;
    }

    while (!startReached)
    {
        size_t previousIndex = backwardIndices[startVertex];
        if (previousIndex != INF)
            startVertex = unsorted_path_[previousIndex].row;
        else
            startReached = true;
    }
    matrix_[endVertex][startVertex] = INF;
}


/**
 * Reduce the cost matrix.
 * @return The sum of reduced values.
 */
cost_t StageState::reduce_cost_matrix() {
    return matrix_.reduce_cols() + matrix_.reduce_rows();
}

/**
 * Given the optimal path, return the optimal cost.
 * @param optimal_path
 * @param m
 * @return Cost of the path.
 */
cost_t get_optimal_cost(const path_t& optimal_path, const cost_matrix_t& m) {
    cost_t cost = 0;

    for (std::size_t idx = 1; idx < optimal_path.size(); ++idx) {
        cost += m[optimal_path[idx - 1] - 1][optimal_path[idx] - 1];
    }

    cost += m[optimal_path[optimal_path.size() - 1] - 1][optimal_path[0] - 1];

    return cost;
}

/**
 * Create the right branch matrix with the chosen vertex forbidden and the new lower bound.
 * @param m
 * @param v
 * @param lb
 * @return New branch.
 */
StageState create_right_branch_matrix(cost_matrix_t m, vertex_t v, cost_t lb) {
    CostMatrix cm(m);
    cm[v.row][v.col] = INF;
    return StageState(cm, {}, lb);
}

/**
 * Retain only optimal ones (from all possible ones).
 * @param solutions
 * @return Vector of optimal solutions.
 */
tsp_solutions_t filter_solutions(tsp_solutions_t solutions) {
    cost_t optimal_cost = INF;
    for (const auto& s : solutions) {
        optimal_cost = (s.lower_bound < optimal_cost) ? s.lower_bound : optimal_cost;
    }

    tsp_solutions_t optimal_solutions;
    std::copy_if(solutions.begin(), solutions.end(),
                 std::back_inserter(optimal_solutions),
                 [&optimal_cost](const tsp_solution_t& s) { return s.lower_bound == optimal_cost; }
    );

    return optimal_solutions;
}

/**
 * Solve the TSP.
 * @param cm The cost matrix.
 * @return A list of optimal solutions.
 */
tsp_solutions_t solve_tsp(const cost_matrix_t& cm) {

    StageState left_branch(cm);

    std::stack<StageState> tree_lifo;

    std::size_t n_levels = cm.size() - 2;

    tree_lifo.push(left_branch);

    cost_t best_lb = INF;
    tsp_solutions_t solutions;

    while (!tree_lifo.empty()) {

        left_branch = tree_lifo.top();
        tree_lifo.pop();

        while (left_branch.get_level() != n_levels && left_branch.get_lower_bound() <= best_lb) {

            if (left_branch.get_level() == 0) {
                left_branch.reset_lower_bound();
            }

            // 1. Reduce the matrix in rows and columns.
            cost_t new_cost = left_branch.reduce_cost_matrix(); // @TODO (KROK 1)

            // 2. Update the lower bound and check the break condition.
            left_branch.update_lower_bound(new_cost);
            if (left_branch.get_lower_bound() > best_lb) {
                break;
            }

            // 3. Get new vertex and the cost of not choosing it.
            NewVertex new_vertex = left_branch.choose_new_vertex(); // @TODO (KROK 2)

            // 4. @TODO Update the path - use append_to_path method.
            left_branch.append_to_path(new_vertex.coordinates);
            
            // 5. @TODO (KROK 3) Update the cost matrix of the left branch.
            left_branch.update_cost_matrix(new_vertex.coordinates);

            // 6. Update the right branch and push it to the LIFO.
            cost_t new_lower_bound = left_branch.get_lower_bound() + new_vertex.cost;
            tree_lifo.push(create_right_branch_matrix(cm, new_vertex.coordinates,
                                                      new_lower_bound));
        }

        if (left_branch.get_lower_bound() <= best_lb) {
            // If the new solution is at least as good as the previous one,
            // save its lower bound and its path.
            best_lb = left_branch.get_lower_bound();
            path_t new_path = left_branch.get_path();
            solutions.push_back({get_optimal_cost(new_path, cm), new_path});
        }
    }

    return filter_solutions(solutions); // Filter solutions to find only optimal ones.
}

